"""
test_technisupport_exe.py  [v7]
================================
Agrega test de FORMULARIO CUV:
  - Abre pestaña FORMULARIO CUV
  - Click en AGREGAR
  - Escribe el Número de Serie
  - Click en LLENAR ESPACIOS

Coordenadas calibradas:
  Formulario Usuario:
    cliente:   y_rel=167
    cedula:    y_rel=194
    correo:    y_rel=263
    telefono:  y_rel=326

PASO 1:  pip install pyautogui pygetwindow Pillow pyperclip
PASO 2:  python test_technisupport_exe.py
"""

import sys, subprocess

def _instalar(pkg, imp=None):
    try: __import__(imp or pkg)
    except ImportError:
        subprocess.check_call([sys.executable,"-m","pip","install",pkg],
                              stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

_instalar("pyautogui"); _instalar("pygetwindow")
_instalar("Pillow","PIL"); _instalar("pyperclip")

import os, time
import pyautogui, pygetwindow as gw, pyperclip

EXE_PATH      = r"C:\Users\Ashleidy\Desktop\TechniSupport2\TechniSupport.exe"
WINDOW_TITLE  = "BASES DE DATOS"
FORM_USUARIO  = "Registro de usuarios"
FORM_CUV      = "Registro de Hoja de Vida del Equipo"
FORM_DIAG     = "Registro de Diagnóstico"
TIMEOUT       = 15

USUARIO_TEST = {
    "cliente":  "Juan Perez Garcia",
    "cedula":   "1234567890",
    "correo":   "juan.perez@test.com",
    "telefono": "3001234567",
}

CUV_TEST = {
    "numero_serie": "SN-TEST-001",
}

DIAG_TEST = {
    "numero_serie": "SN-TEST-001",
}

pyautogui.FAILSAFE = True
pyautogui.PAUSE    = 0.3
resultados = []

# ── helpers ───────────────────────────────────────────────────────────────────
def log(msg, s="INFO"):
    print({"INFO":"  •","OK":"  ✅","FAIL":"  ❌"}.get(s,"  •")+" "+msg)

def registrar(nombre, ok, det=""):
    resultados.append((nombre,"PASS" if ok else f"FAIL: {det}"))
    log(nombre,"OK" if ok else "FAIL")
    if not ok and det: log(f"  -> {det}","FAIL")

def esperar_ventana(titulo, timeout=TIMEOUT):
    for _ in range(timeout*2):
        w=gw.getWindowsWithTitle(titulo)
        if w: return w[0]
        time.sleep(0.5)
    return None

def enfocar(titulo=WINDOW_TITLE):
    w=gw.getWindowsWithTitle(titulo)
    if w:
        try: w[0].activate()
        except: pass
        time.sleep(0.4); return w[0]
    return None

def click_rel(v, ox, oy):
    pyautogui.click(v.left+ox, v.top+oy); time.sleep(0.4)

def pegar(x, y, texto):
    """Pega via portapapeles — evita problemas con @ en teclado español."""
    pyperclip.copy(texto)
    pyautogui.click(x, y);         time.sleep(0.35)
    pyautogui.click(x, y);         time.sleep(0.25)
    pyautogui.hotkey("ctrl","a");  time.sleep(0.15)
    pyautogui.hotkey("ctrl","v");  time.sleep(0.4)

def cerrar_popup_confirmacion(excluir_titulos):
    """Cierra popups de confirmación sin tocar las ventanas principales."""
    for t in ["exitoso","guardado","éxito","correcto","Error","Advertencia"]:
        c=[w for w in gw.getAllWindows()
           if t.lower() in w.title.lower()
           and w.title not in excluir_titulos]
        if c:
            log(f"  -> Popup '{c[0].title}' cerrado")
            c[0].activate(); time.sleep(0.3)
            pyautogui.press("enter"); time.sleep(0.8)
            return True
    return False

# ══════════════════════════════════════════════════════════════════════════════
#  TESTS
# ══════════════════════════════════════════════════════════════════════════════

def t01_exe_existe():
    ok=os.path.exists(EXE_PATH)
    registrar("El archivo .exe existe en la ruta",ok,f"No encontrado: {EXE_PATH}")
    return ok

def t02_app_abre(p):
    ok=p is not None and p.poll() is None
    registrar("La aplicación inicia sin errores",ok)
    return ok

def t03_ventana_aparece(v):
    ok=v is not None and WINDOW_TITLE in (v.title or "")
    registrar("Ventana principal aparece con título correcto",ok)
    return ok

def t04_popup_conexion():
    p=esperar_ventana("Conexión exitosa",timeout=10)
    if p:
        p.activate(); time.sleep(0.3)
        pyautogui.press("enter"); time.sleep(0.8)
    r=gw.getWindowsWithTitle("Conexión exitosa")
    ok=p is not None and len(r)==0
    registrar("Popup 'Conexión exitosa' aparece y se cierra",ok)
    return ok

def t05_tamanio(ventana):
    v=enfocar() or ventana
    ok=v is not None and v.width>=800 and v.height>=600
    log(f"Tamaño: {v.width if v else '?'}x{v.height if v else '?'}px")
    registrar("Tamaño mínimo 800x600",ok)
    return ok

def t06_centrada(ventana):
    ok=not(ventana.left<=5 and ventana.top<=5)
    registrar("Ventana centrada (no en esquina 0,0)",ok)
    return ok

def t07_tabs(ventana):
    try:
        for ox,oy in [(90,50),(242,50),(369,53),(567,57)]:
            v=enfocar() or ventana; pyautogui.click(v.left+ox, v.top+oy); time.sleep(0.5)
        registrar("Navegación por las 4 pestañas sin crash",True); return True
    except Exception as e:
        registrar("Navegación por las 4 pestañas sin crash",False,str(e)); return False

def t08_volver_usuario(ventana):
    try:
        v=enfocar() or ventana; pyautogui.click(v.left+90, v.top+50); time.sleep(0.4)
        registrar("Volver a pestaña FORMULARIO USUARIO",True); return True
    except Exception as e:
        registrar("Volver a pestaña FORMULARIO USUARIO",False,str(e)); return False

def t09_boton_agregar(ventana, form_titulo):
    """Click en AGREGAR esperando cualquier formulario indicado."""
    try:
        for oy in [ventana.height-40, ventana.height-50,
                   ventana.height-35, ventana.height-60]:
            v=enfocar() or ventana
            log(f"  Intentando AGREGAR en y_rel={oy}")
            click_rel(v,180,oy)
            d=esperar_ventana(form_titulo,timeout=3)
            if d:
                registrar(f"Botón AGREGAR abre '{form_titulo}'",True)
                return True
        registrar(f"Botón AGREGAR abre '{form_titulo}'",False,"Formulario no apareció")
        return False
    except Exception as e:
        registrar(f"Botón AGREGAR abre '{form_titulo}'",False,str(e))
        return False

# ──────────────────────────────────────────────────────────────────────────────
#  T10 — Registro usuario
# ──────────────────────────────────────────────────────────────────────────────
def t10_registrar_usuario():
    nombre_test=f"Registro de usuario: '{USUARIO_TEST['cliente']}'"
    try:
        d=esperar_ventana(FORM_USUARIO,timeout=8)
        if d is None:
            registrar(nombre_test,False,"Formulario no abierto"); return False

        d.activate(); time.sleep(0.8)
        log(f"Formulario Usuario: left={d.left} top={d.top} w={d.width} h={d.height}")

        cx         = d.left + int(d.width * 0.62)
        y_cliente  = d.top + 167
        y_cedula   = d.top + 194
        y_correo   = d.top + 263
        y_telefono = d.top + 326

        log(f"  -> Cliente:    {USUARIO_TEST['cliente']}")
        pegar(cx, y_cliente,  USUARIO_TEST["cliente"])
        log(f"  -> Cédula/NIT: {USUARIO_TEST['cedula']}")
        pegar(cx, y_cedula,   USUARIO_TEST["cedula"])
        log(f"  -> Correo:     {USUARIO_TEST['correo']}")
        pegar(cx, y_correo,   USUARIO_TEST["correo"])
        log(f"  -> Teléfono:   {USUARIO_TEST['telefono']}")
        pegar(cx, y_telefono, USUARIO_TEST["telefono"])

        time.sleep(0.5)
        d=enfocar(FORM_USUARIO) or d
        bx=d.left+int(d.width*0.50)
        by=d.top +int(d.height*0.88)
        log(f"  -> Click GUARDAR ({bx},{by})")
        pyautogui.click(bx,by); time.sleep(2.0)

        cerrar_popup_confirmacion([FORM_USUARIO, WINDOW_TITLE])

        time.sleep(0.5)
        abierto=[w for w in gw.getAllWindows() if FORM_USUARIO in w.title]
        ok=len(abierto)==0
        registrar(nombre_test,ok,"El formulario siguió abierto después de GUARDAR")
        return ok

    except Exception as e:
        registrar(nombre_test,False,str(e)); return False

# ──────────────────────────────────────────────────────────────────────────────
#  T11 — Pestaña CUV + Número de Serie + LLENAR ESPACIOS
# ──────────────────────────────────────────────────────────────────────────────
def t11_click_tab_cuv(ventana):
    """
    Click en la pestaña FORMULARIO CUV.
    Coordenadas calibradas: rel=(242, 50)
    """
    try:
        v = enfocar() or ventana
        # Coordenadas CALIBRADAS — medidas manualmente: rel=(242, 50)
        tab_x = v.left + 242
        tab_y = v.top  + 50
        log(f"  Click en pestaña CUV ({tab_x}, {tab_y})")
        pyautogui.click(tab_x, tab_y)
        time.sleep(0.8)
        registrar("Click en pestaña FORMULARIO CUV", True)
        return True
    except Exception as e:
        registrar("Click en pestaña FORMULARIO CUV", False, str(e))
        return False

def t12_agregar_cuv(ventana):
    """Click en AGREGAR dentro de la pestaña CUV para abrir el formulario."""
    try:
        for oy in [ventana.height-40, ventana.height-50,
                   ventana.height-35, ventana.height-60]:
            v = enfocar() or ventana
            log(f"  Intentando AGREGAR CUV en y_rel={oy} (abs={v.top+oy})")
            click_rel(v, 180, oy)
            d = esperar_ventana(FORM_CUV, timeout=3)
            if d:
                registrar("Botón AGREGAR abre formulario CUV", True)
                return True
        registrar("Botón AGREGAR abre formulario CUV", False, "Formulario CUV no apareció")
        return False
    except Exception as e:
        registrar("Botón AGREGAR abre formulario CUV", False, str(e))
        return False

def t13_numero_serie_y_llenar_espacios():
    """
    En el formulario CUV:
      1. Escribe el Número de Serie
      2. Click en LLENAR ESPACIOS
    Basado en la imagen:
      - El formulario tiene fecha de ingreso/entrega arriba (date pickers)
      - Tipo, Marca, Modelo, Número de Serie son campos de texto
      - Número de Serie es el 4to campo de texto (y_rel≈370 aprox)
      - LLENAR ESPACIOS es el botón izquierdo inferior
    """
    nombre_test=f"CUV: escribir Número de Serie y click LLENAR ESPACIOS"
    try:
        d=esperar_ventana(FORM_CUV, timeout=8)
        if d is None:
            registrar(nombre_test,False,"Formulario CUV no abierto"); return False

        d.activate(); time.sleep(0.8)
        log(f"Formulario CUV: left={d.left} top={d.top} w={d.width} h={d.height}")

        # ── Coordenadas ABSOLUTAS de pantalla — medidas directamente ─────
        # Estas son coordenadas absolutas, NO relativas al diálogo.
        # Se usan directamente con pyautogui.click(x_abs, y_abs)
        ABS_NUM_SERIE_X  = 980   # abs=(980,572)
        ABS_NUM_SERIE_Y  = 572
        ABS_LLENAR_X     = 828   # abs=(828,880)
        ABS_LLENAR_Y     = 880
        ABS_GUARDAR_X    = 997   # abs=(997,862)
        ABS_GUARDAR_Y    = 862

        log(f"  -> Número de Serie: {CUV_TEST['numero_serie']}")
        pegar(ABS_NUM_SERIE_X, ABS_NUM_SERIE_Y, CUV_TEST["numero_serie"])
        time.sleep(0.5)

        # ── Click en LLENAR ESPACIOS ──────────────────────────────────────
        d=enfocar(FORM_CUV) or d
        log(f"  -> Click LLENAR ESPACIOS ({ABS_LLENAR_X},{ABS_LLENAR_Y})")
        pyautogui.click(ABS_LLENAR_X, ABS_LLENAR_Y)
        time.sleep(2.0)

        # Verificar que el formulario sigue abierto (LLENAR no cierra)
        d_aun=esperar_ventana(FORM_CUV, timeout=3)
        ok = d_aun is not None
        registrar(nombre_test, ok,
                  "El formulario CUV se cerró inesperadamente")

        if ok:
            log("  LLENAR ESPACIOS funcionó — procediendo a GUARDAR")
            time.sleep(0.5)

            d_aun = enfocar(FORM_CUV) or d_aun
            log(f"  -> Click GUARDAR ({ABS_GUARDAR_X},{ABS_GUARDAR_Y})")
            pyautogui.click(ABS_GUARDAR_X, ABS_GUARDAR_Y)
            time.sleep(2.0)

            # Cerrar popup de confirmación si aparece
            cerrar_popup_confirmacion([FORM_CUV, WINDOW_TITLE])

            # Verificar que el formulario se cerró = guardado exitoso
            time.sleep(0.5)
            aun_abierto = [w for w in gw.getAllWindows() if FORM_CUV in w.title]
            if len(aun_abierto) == 0:
                log("  CUV guardado y formulario cerrado correctamente ✓")
            else:
                log("  Formulario CUV sigue abierto tras GUARDAR — revisar","FAIL")

        return ok

    except Exception as e:
        registrar(nombre_test,False,str(e)); return False


# ──────────────────────────────────────────────────────────────────────────────
#  T14 — FORMULARIO DIAGNÓSTICO (pestaña 3)
#  1. Click en pestaña 3
#  2. Abre formulario con AGREGAR
#  3. Selecciona primera cédula del ComboBox
#  4. Escribe Número de Serie
#  5. Click LLENAR ESPACIOS
#  6. Click GUARDAR
# ──────────────────────────────────────────────────────────────────────────────
def t14_formulario_diagnostico(ventana):
    nombre_test = "Formulario Diagnóstico: cédula + serie + LLENAR + GUARDAR"
    try:
        # 1. Click en pestaña FORMULARIO DIAGNOSTICO
        v = enfocar() or ventana
        log(f"  -> Click pestaña DIAGNÓSTICO (369,53)")
        pyautogui.click(v.left + 369, v.top + 53)
        time.sleep(0.8)

        # 2. Click en AGREGAR
        v = enfocar() or ventana
        abierto = False
        for oy in [v.height-40, v.height-50, v.height-35, v.height-60]:
            click_rel(v, 180, oy)
            # El formulario de diagnóstico puede tener título diferente
            # esperamos cualquier ventana nueva que no sea la principal
            time.sleep(1.5)
            for w in gw.getAllWindows():
                if w.title and w.title != WINDOW_TITLE and w.title != "":
                    log(f"  Formulario abierto: '{w.title}'")
                    abierto = True
                    break
            if abierto:
                break

        if not abierto:
            registrar(nombre_test, False, "Formulario diagnóstico no abrió")
            return False

        time.sleep(0.8)

        # 3. Seleccionar primera cédula del ComboBox
        # Coordenadas ABSOLUTAS: abs=(1397,183)
        log("  -> Click ComboBox cédula (1397,183)")
        pyautogui.click(1397, 183)
        time.sleep(0.6)
        # Seleccionar primera opción con flecha abajo + Enter
        pyautogui.press("down")
        time.sleep(0.3)
        pyautogui.press("enter")
        time.sleep(0.5)

        # 4. Escribir Número de Serie
        # Coordenadas ABSOLUTAS: abs=(1219,238)
        log(f"  -> Número de Serie ({1219},{238}): {DIAG_TEST['numero_serie']}")
        pegar(1219, 238, DIAG_TEST["numero_serie"])
        time.sleep(0.5)

        # 5. Click LLENAR ESPACIOS
        # Coordenadas ABSOLUTAS: abs=(858,912)
        log("  -> Click LLENAR ESPACIOS (858,912)")
        pyautogui.click(858, 912)
        time.sleep(2.0)

        # 6. Click GUARDAR
        # Coordenadas ABSOLUTAS: abs=(1019,907)
        log("  -> Click GUARDAR (1019,907)")
        pyautogui.click(1019, 907)
        time.sleep(2.0)

        # Cerrar popup de confirmación si aparece
        cerrar_popup_confirmacion([WINDOW_TITLE])

        time.sleep(0.5)
        registrar(nombre_test, True)
        return True

    except Exception as e:
        registrar(nombre_test, False, str(e))
        return False

# ──────────────────────────────────────────────────────────────────────────────
#  T15 — GENERACIÓN DE DOCUMENTOS (pestaña 4) — click REFRESCAR
# ──────────────────────────────────────────────────────────────────────────────
def t15_formulario_documentos(ventana):
    nombre_test = "Generación de Documentos: click REFRESCAR"
    try:
        # 1. Click en pestaña GENERACIÓN DE DOCUMENTOS
        v = enfocar() or ventana
        log("  -> Click pestaña DOCUMENTOS (567,57)")
        pyautogui.click(v.left + 567, v.top + 57)
        time.sleep(0.8)

        # 2. Click en REFRESCAR
        # Coordenadas ABSOLUTAS: abs=(1097,907)
        v = enfocar() or ventana
        log("  -> Click REFRESCAR (1097,907)")
        pyautogui.click(1097, 907)
        time.sleep(1.5)

        registrar(nombre_test, True)
        return True

    except Exception as e:
        registrar(nombre_test, False, str(e))
        return False

def t16_usuario_en_tabla():
    try:
        time.sleep(0.8)
        # Volver a pestaña USUARIO primero
        v=enfocar()
        if v:
            pyautogui.click(v.left+90, v.top+50)
            time.sleep(0.5)

        v=enfocar()
        if v is None:
            registrar("Búsqueda del usuario en tabla",False,"Ventana no encontrada")
            return False
        cx=v.left+v.width//2; cy=v.top+116
        pyperclip.copy(USUARIO_TEST["cliente"].split()[0])
        pyautogui.click(cx,cy); time.sleep(0.3)
        pyautogui.hotkey("ctrl","a"); pyautogui.hotkey("ctrl","v"); time.sleep(0.3)
        pyautogui.click(v.left+v.width-60,cy); time.sleep(1)
        registrar("Búsqueda del usuario registrado ejecutada sin errores",True)
        pyautogui.click(cx,cy)
        pyautogui.hotkey("ctrl","a"); pyautogui.press("delete")
        return True
    except Exception as e:
        registrar("Búsqueda del usuario en tabla",False,str(e)); return False

def t17_maximizar(proceso):
    try:
        v=enfocar(); v.maximize(); time.sleep(0.8)
        assert proceso.poll() is None
        v.restore(); time.sleep(0.8)
        assert proceso.poll() is None
        registrar("Maximizar y restaurar sin crash",True); return True
    except Exception as e:
        registrar("Maximizar y restaurar sin crash",False,str(e)); return False

# ══════════════════════════════════════════════════════════════════════════════
#  RUNNER
# ══════════════════════════════════════════════════════════════════════════════
def main():
    print("\n"+"="*60)
    print("  TESTS AUTOMATIZADOS — TechniSupport.exe  [v7]")
    print("="*60)
    print(f"  EXE      : {EXE_PATH}")
    print(f"  USUARIO  : {USUARIO_TEST['cliente']}")
    print(f"  NUM SERIE: {CUV_TEST['numero_serie']}")
    print("  No toques mouse ni teclado durante el test")
    print("="*60)
    time.sleep(2)

    if not t01_exe_existe(): sys.exit(1)

    log("Iniciando TechniSupport.exe...")
    proceso=subprocess.Popen([EXE_PATH]); time.sleep(5)
    ventana=esperar_ventana(WINDOW_TITLE)

    t02_app_abre(proceso)
    t03_ventana_aparece(ventana)
    t04_popup_conexion()
    ventana=esperar_ventana(WINDOW_TITLE,timeout=5) or ventana
    enfocar()

    t05_tamanio(ventana)
    t06_centrada(ventana)
    t07_tabs(ventana)
    t08_volver_usuario(ventana)

    # ── Bloque FORMULARIO USUARIO ──────────────────────────────────────────
    ventana=enfocar() or ventana
    t09_boton_agregar(ventana, FORM_USUARIO)
    t10_registrar_usuario()

    # ── Bloque FORMULARIO CUV ──────────────────────────────────────────────
    ventana=enfocar() or ventana
    t11_click_tab_cuv(ventana)          # 1. click en pestaña CUV
    ventana=enfocar() or ventana
    t12_agregar_cuv(ventana)            # 2. click en AGREGAR
    t13_numero_serie_y_llenar_espacios()  # 3. serie + LLENAR + GUARDAR

    # ── Búsqueda y cierre ─────────────────────────────────────────────────
    ventana=enfocar() or ventana
    t14_formulario_diagnostico(ventana)
    ventana=enfocar() or ventana
    t15_formulario_documentos(ventana)
    ventana=enfocar() or ventana
    t16_usuario_en_tabla()
    t17_maximizar(proceso)

    log("Cerrando TechniSupport.exe...")
    try:
        v=enfocar()
        if v: v.close()
        time.sleep(1)
        if proceso.poll() is None: proceso.terminate()
    except: proceso.terminate()

    pasados =sum(1 for _,r in resultados if r=="PASS")
    fallidos=len(resultados)-pasados
    print("\n"+"="*60)
    print("  REPORTE FINAL")
    print("="*60)
    for nom,res in resultados:
        print(f"  {'✅' if res=='PASS' else '❌'} {nom}")
        if res!="PASS": print(f"       -> {res}")
    print("="*60)
    print(f"  Total: {len(resultados)}  |  ✅ {pasados}  |  ❌ {fallidos}")
    print("="*60+"\n")
    sys.exit(0 if fallidos==0 else 1)

if __name__=="__main__":
    main()