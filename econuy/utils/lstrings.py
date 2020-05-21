import datetime as dt

beef_url = (
    "https://www.inac.uy/innovaportal/v/9799/10/innova.front/serie-semanal"
    "-ingreso-medio-de-exportacion---bovino-ovino-y-otros-productos")
pulp_url = (
    f"https://www.insee.fr/en/statistiques/serie/telecharger/010600339?ordre=antechronologique&"
    f"transposition=donneescolonne&periodeDebut=1&anneeDebut=1990&periodeFin=11&anneeFin="
    f"{dt.datetime.now().year}")
soybean_url = "https://www.quandl.com/api/v3/datasets/CHRIS/CME_S1.csv?api_key=3TPxACcrxy9WsE871Lqe"
what_url = "https://www.quandl.com/api/v3/datasets/CHRIS/CME_W1.csv?api_key=3TPxACcrxy9WsE871Lqe"
imf_url = "https://www.imf.org/~/media/Files/Research/CommodityPrices/Monthly/ExternalData.ashx"
milk1_url = "https://www.inale.org/estadisticas/"
milk2_url = "https://ec.europa.eu/info/sites/info/files/food-farming-fisheries/farming/documents/eu-milk-historical-price-series_en.xls"
cpi_url = "http://ine.gub.uy/c/document_library/get_file?uuid=2e92084a-94ec-4fec-b5ca-42b40d5d2826&groupId=10181"
nxr_url = "http://ine.gub.uy/c/document_library/get_file?uuid=3fbf4ffd-a829-420c-aca9-9f01ecd7919a&groupId=10181"
nxr_daily_url = "https://www.bcu.gub.uy/_layouts/BCU.Cotizaciones/handler/FileHandler.ashx?op=downloadcotizacionesexcel&KeyValuePairs={%22KeyValuePairs%22:{%22Monedas%22:[{%22Val%22:%222224%22,%22Text%22:%22DLS.%20USA%20CABLE%22}],"
labor_url = "http://ine.gub.uy/c/document_library/get_file?uuid=50ae926c-1ddc-4409-afc6-1fecf641e3d0&groupId=10181"
wages1_url = "http://www.ine.gub.uy/c/document_library/get_file?uuid=a76433b7-5fba-40fc-9958-dd913338e989&groupId=10181"
wages2_url = "http://www.ine.gub.uy/c/document_library/get_file?uuid=97f07fd8-9410-476e-bf81-e6b1c11467ef&groupId=10181"
wap_url = "http://www.ine.gub.uy/c/document_library/get_file?uuid=2a5c1e6e-b02f-4a63-963f-925edea7c17e&groupId=10181"
ff_url = "https://www.bcu.gub.uy/Politica-Economica-y-Mercados/Mercado%20de%20Cambios/informepublico"
fiscal_url = "https://www.gub.uy/ministerio-economia-finanzas/datos-y-estadisticas/datos"
reserves_url = "https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Informe%20Diario%20Pasivos%20Monetarios/infd_"
reer_url = "https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Paginas/Cambio-Real-Efectivo.aspx"
missing_reserves_url = "https://docs.google.com/spreadsheets/d/1tXwv8SaigbBrfBSSCVGBjSs88f3dgTq4nIANPn7vjYI/export?format=xlsx&authuser=0"
ar_cpi_url = "http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables_datos.asp"
ar_cpi_payload = "fecha_desde=1970-01-01&fecha_hasta=2019-12-31&B1=Enviar&primeravez=1&fecha_desde=19600101&fecha_hasta=20191231&serie=7931&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Inflaci%F3n+mensual%A0%28variaci%F3n+en+%29"

fiscal_sheets = {
    "Sector Público No Financiero":
        {"Name": "nfps",
         "Colnames": ["Ingresos: SPNF",
                      "Ingresos: Gobierno central",
                      "Ingresos: DGI", "Ingresos: IRP",
                      "Ingresos: Comercio ext.",
                      "Ingresos: Otros", "Ingresos: BPS",
                      "Ingresos: Res. primario corriente EEPP",
                      "Egresos: Primarios SPNF",
                      "Egresos: Primarios corrientes GC-BPS",
                      "Egresos: Remuneraciones",
                      "Egresos: No personales",
                      "Egresos: Pasividades",
                      "Egresos: Transferencias",
                      "Egresos: Inversiones",
                      "Resultado: Primario intendencias",
                      "Resultado: Primario BSE",
                      "Resultado: Primario SPNF",
                      "Intereses: Totales", "Intereses: GC-BPS",
                      "Intereses: EEPP",
                      "Intereses: Intendencias",
                      "Intereses: BSE",
                      "Resultado: Global SPNF"]},
    "Sector Público Consolidado":
        {"Name": "gps",
         "Colnames": ["Resultado: Primario SPNF",
                      "Intereses: SPNF", "Resultado: Global SPNF",
                      "Resultado: Primario BCU", "Intereses: BCU",
                      "Resultado: Global BCU",
                      "Resultado: Primario SPC",
                      "Resultado: Global SPC"]},
    "Gobierno Central - BPS":
        {"Name": "gc-bps",
         "Colnames": ["Ingresos: GC-BPS", "Ingresos: GC",
                      "Ingresos: Comercio ext.", "Ingresos: DGI",
                      "Ingresos: DGI bruto", "Ingresos: DGI CDI",
                      "Ingresos: Loterías",
                      "Ingresos: Venta energía",
                      "Ingresos: TGN/otros", "Ingresos: FIMTOP",
                      "Ingresos: Aportes EEPP", "Ingresos: IRP",
                      "Ingresos: Rec. Lib. Disp",
                      "Ingresos: BPS neto", "Ingresos: BPS bruto",
                      "Ingresos: FSS",
                      "Ingresos: BPS CDI", "Ingresos: BPS otros",
                      "Egresos: GC-BPS",
                      "Egresos: Remuneraciones",
                      "Egresos: Remuneraciones adm. central",
                      "Egresos: Remuneraciones org. docentes",
                      "Egresos: Remuneraciones retenc./otros",
                      "Egresos: Remuneraciones BPS",
                      "Egresos: Pasividades",
                      "Egresos: Pasividades Caja Policial",
                      "Egresos: Pasividades Caja Militar",
                      "Egresos: Pasividades BPS",
                      "Egresos: No personales",
                      "Egresos: No personales adm. central",
                      "Egresos: No personales org. docentes",
                      "Egresos: No personales suministros",
                      "Egresos: No personales plan emergencia",
                      "Egresos: No personales BPS",
                      "Egresos: Transferencias",
                      "Egresos: Transferencias GC",
                      "Egresos: Transferencias GC Entes",
                      "Egresos: Transferencias GC deuda",
                      "Egresos: Transferencias GC otros org.",
                      "Egresos: Transferencias GC rentas afectadas",
                      "Egresos: Transferencias BPS",
                      "Egresos: Transferencias BPS enfermedad",
                      "Egresos: Transferencias BPS AFAM y otras prestaciones",
                      "Egresos: Transferencias BPS desempleo",
                      "Egresos: Transferencias BPS 2",
                      "Egresos: Transferencias BPS -IRP/IRPF",
                      "Egresos: Transferencias BPS AFAP",
                      "Egresos: Transferencias BPS otros",
                      "Egresos: Transferencias otros",
                      "Egresos: Inversión",
                      "Egresos: Inversión MTOP",
                      "Egresos: Inversión MVOTMA",
                      "Egresos: Inversión Presidencia",
                      "Egresos: Inversión org. docentes",
                      "Egresos: Inversión resto",
                      "Intereses: Total", "Intereses: GC",
                      "Intereses: BPS-FSS",
                      "Resultado: Global GC-BPS"]},
    "Empresas Públicas Consolidado":
        {"Name": "pe",
         "Colnames": ["Ingresos",
                      "Ingresos: Venta bienes y servicios",
                      "Ingresos: Otros",
                      "Ingresos: Transferencias GC", "Egresos",
                      "Egresos: Corrientes",
                      "Egresos: Remuneraciones",
                      "Egresos: Compras bienes y servicios",
                      "Egresos: Intereses", "Egresos: DGI",
                      "Egresos: BPS",
                      "Egresos: No corrientes",
                      "Egresos: Inversiones",
                      "Egresos: Dividendo",
                      "Resultado: Global"]},
    "ANCAP":
        {"Name": "ancap",
         "Colnames": ["Ingresos",
                      "Ingresos: Venta bienes y servicios",
                      "Ingresos: Otros",
                      "Ingresos: Transferencias GC", "Egresos",
                      "Egresos: Corrientes",
                      "Egresos: Remuneraciones",
                      "Egresos: Compras bienes y servicios",
                      "Egresos: Intereses", "Egresos: DGI",
                      "Egresos: BPS",
                      "Egresos: No corrientes",
                      "Egresos: Inversiones",
                      "Egresos: Var. stock petróleo",
                      "Egresos: Otros", "Egresos: Dividendo",
                      "Resultado: Global"]},
    "ANTEL":
        {"Name": "antel",
         "Colnames": ["Ingresos",
                      "Ingresos: Venta bienes y servicios",
                      "Ingresos: Otros",
                      "Ingresos: Transferencias GC", "Egresos",
                      "Egresos: Corrientes",
                      "Egresos: Remuneraciones",
                      "Egresos: Compras bienes y servicios",
                      "Egresos: Intereses", "Egresos: DGI",
                      "Egresos: BPS",
                      "Egresos: No corrientes",
                      "Egresos: Inversiones",
                      "Egresos: Dividendo", "Resultado: Global"]},
    "OSE":
        {"Name": "ose",
         "Colnames": ["Ingresos",
                      "Ingresos: Venta bienes y servicios",
                      "Ingresos: Otros",
                      "Ingresos: Transferencias GC", "Egresos",
                      "Egresos: Corrientes",
                      "Egresos: Remuneraciones",
                      "Egresos: Compras bienes y servicios",
                      "Egresos: Intereses", "Egresos: DGI",
                      "Egresos: BPS",
                      "Egresos: No corrientes",
                      "Egresos: Inversiones",
                      "Egresos: Dividendo",
                      "Resultado: Global"]},
    "UTE":
        {"Name": "ute",
         "Colnames": ["Ingresos",
                      "Ingresos: Venta bienes y servicios",
                      "Ingresos: Otros",
                      "Ingresos: Transferencias GC", "Egresos",
                      "Egresos: Corrientes",
                      "Egresos: Remuneraciones",
                      "Egresos: Compras bienes y servicios",
                      "Egresos: Intereses", "Egresos: DGI",
                      "Egresos: BPS",
                      "Egresos: No corrientes",
                      "Egresos: Inversiones",
                      "Egresos: Dividendo",
                      "Resultado: Global"]}
}

nat_accounts_metadata = {
    "https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Cuentas%20Nacionales/cuadro_101t.xls":
        {"Rows": 12, "Inf. Adj.": "Const. 2005", "Unit": "Miles", "Seas": "NSA",
         "Name": "ind_con_nsa",
         "Colnames": ["PBI: Actividades primarias",
                      "PBI: Agricultura, ganadería, caza y silvucultura",
                      "PBI: Industrias manufactureras",
                      "PBI: Suministro de electricidad, gas y agua",
                      "PBI: Construcción",
                      "PBI: Comercio, reparaciones, restaurantes y hoteles",
                      "PBI: Transporte, almacenamiento y comunicaciones",
                      "PBI: Otras actividades",
                      "PBI: SIFMI", "PBI: Impuestos menos subvenciones",
                      "PBI"]},
    "https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Cuentas%20Nacionales/cuadro_100t.xls":
        {"Rows": 12, "Inf. Adj.": "No", "Unit": "Miles", "Seas": "NSA",
         "Name": "ind_cur_nsa",
         "Colnames": ["PBI: Actividades primarias",
                      "PBI: Agricultura, ganadería, caza y silvucultura",
                      "PBI: Industrias manufactureras",
                      "PBI: Suministro de electricidad, gas y agua",
                      "PBI: Construcción",
                      "PBI: Comercio, reparaciones, restaurantes y hoteles",
                      "PBI: Transporte, almacenamiento y comunicaciones",
                      "PBI: Otras actividades",
                      "PBI: SIFMI", "PBI: Impuestos menos subvenciones",
                      "PBI"]},
    "https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Cuentas%20Nacionales/cuadro_104t.xls":
        {"Rows": 10, "Inf. Adj.": "Const. 2005", "Unit": "Miles", "Seas": "NSA",
         "Name": "gas_con_nsa",
         "Colnames": ["PBI: Gasto total", "PBI: Gasto privado",
                      "PBI: Gasto público",
                      "PBI: Formación bruta de capital",
                      "PBI: Formación bruta de capital fijo",
                      "PBI: Formación bruta de capital fijo pública",
                      "PBI: Formación bruta de capital fijo privada",
                      "PBI: Exportaciones",
                      "PBI: Importaciones", "PBI"]},
    "https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Cuentas%20Nacionales/cuadro_132t.xls":
        {"Rows": 12, "Inf. Adj.": "Const. 2005", "Unit": "2005=100",
         "Seas": "NSA", "Name": "ind_con_idx_nsa",
         "Colnames": ["PBI: Actividades primarias",
                      "PBI: Agricultura, ganadería, caza y silvucultura",
                      "PBI: Industrias manufactureras",
                      "PBI: Suministro de electricidad, gas y agua",
                      "PBI: Construcción",
                      "PBI: Comercio, reparaciones, restaurantes y hoteles",
                      "PBI: Transporte, almacenamiento y comunicaciones",
                      "PBI: Otras actividades",
                      "PBI: SIFMI", "PBI: Impuestos menos subvenciones",
                      "PBI"]},
    "https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Cuentas%20Nacionales/cuadro_133t.xls":
        {"Rows": 12, "Inf. Adj.": "Const. 2005", "Unit": "2005=100",
         "Seas": "SA", "Name": "ind_con_idx_sa",
         "Colnames": ["PBI: Actividades primarias",
                      "PBI: Agricultura, ganadería, caza y silvucultura",
                      "PBI: Industrias manufactureras",
                      "PBI: Suministro de electricidad, gas y agua",
                      "PBI: Construcción",
                      "PBI: Comercio, reparaciones, restaurantes y hoteles",
                      "PBI: Transporte, almacenamiento y comunicaciones",
                      "PBI: Otras actividades",
                      "PBI: SIFMI", "PBI: Impuestos menos subvenciones",
                      "PBI"]},
    "https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Cuentas%20Nacionales/cuadro_130t.xls":
        {"Rows": 2, "Inf. Adj.": "No", "Unit": "Miles", "Seas": "NSA",
         "Name": "gdp_cur_nsa",
         "Colnames": ["PBI"]}}

reserves_cols = [
    'SALDO AL INICIO DEL PERÍODO', '1. Compras netas de moneda extranjera',
    '1.1. Compras netas en el mercado',
    '1.2. Integración en dólares de valores del BCU ',
    '1.3. Prefinanciación de exportaciones',
    '1.4. Cancelación de contratos forward', '1.5. Gobierno Central',
    '1.5.1. Utilizaciones de préstamos internacionales',
    '1.5.2. Otras compras netas al Gobierno Central',
    '1.6. Otros', '2. Depósitos del Sistema Bancario en el Banco Central',
    '2.1. Banca pública',
    '2.2. Banca privada', '3.- Otros Depósitos en el Banco Central',
    '3.1. Depósitos de otras empresas de intermediación financiera ',
    '3.2. Depósitos de casas de cambio y otras Instituciones',
    '3.3. Depósitos de empresas públicas y gobiernos departamentales',
    '4. Divisas de exportación a liquidar',
    '5.- Obligaciones netas en moneda extranjera con Gobierno Central   ',
    '5.1. Colocación neta de bonos y letras  ', '5.1.1. Colocación bruta',
    '5.1.2. Amortizaciones  ',
    '5.1.3. Intereses y comisiones',
    '5.2. Otras obligaciones netas en moneda extranjera  ',
    '5.2.1. Desembolsos de préstamos internacionales',
    '5.2.2. Servicio neto de préstamos internacionales',
    '5.3.3. Utilizaciones de préstamos internacionales',
    '5.4.5. Aporte de entes a cuenta de resultados',
    '5.4.6.  Compras de moneda extranjera',
    '5.4.7. Giros hacia y desde el BROU',
    '5.4.8. Integración en dólares de tíulos en UI y pesos (neto)',
    '5.4.9. Otros', '6.- Intereses netos',
    '6.1.Intereses pagados sobre depósitos del sistema financiero',
    '6.2. Intereses cobrados sobre fondos colocados en el exterior',
    '6.3. Otros intereses y comisiones netos',
    '7.- Otros', '7.1.  Préstamos y financiamientos empresas públicas',
    '7.2. Cuentas con organismos internacionales',
    ' 7.3. Fondos administrados', '7.4. Diferencias de arbitraje',
    '7.5. Diferencias de cotización e intereses devengados',
    '7.6. Depósitos especiales Clearstream Banking ',
    '7.7. Solicitudes de giro al exterior en trámite', '7.8. Otros',
    'VARIACIÓN TOTAL DEL PERÍODO (1+2+3+4+5+6+7)',
    'SALDO AL FINAL  DEL PERÍODO'
]

fiscal_metadata = {
    "gps": {True: ["Ingresos: SPNF-SPC aj. FSS", "Egresos: Primarios SPNF-SPC",
                   "Egresos: Inversiones SPNF-SPC", "Intereses: SPC aj. FSS",
                   "Egresos: Totales SPC aj. FSS",
                   "Resultado: Primario intendencias",
                   "Resultado: Primario BSE", "Resultado: Primario BCU",
                   "Resultado: Primario SPC aj. FSS",
                   "Resultado: Global SPC aj. FSS"],
            False: ["Ingresos: SPNF-SPC", "Egresos: Primarios SPNF-SPC",
                    "Egresos: Inversiones SPNF-SPC",
                    "Intereses: SPC", "Egresos: Totales SPC",
                    "Resultado: Primario intendencias",
                    "Resultado: Primario BSE", "Resultado: Primario BCU",
                    "Resultado: Primario SPC",
                    "Resultado: Global SPC"]},
    "nfps": {
        True: ["Ingresos: SPNF-SPC aj. FSS", "Egresos: Primarios SPNF-SPC",
               "Egresos: Inversiones SPNF-SPC", "Intereses: SPNF aj. FSS",
               "Egresos: Totales SPNF aj. FSS",
               "Resultado: Primario intendencias",
               "Resultado: Primario BSE", "Resultado: Primario SPNF aj. FSS",
               "Resultado: Global SPNF aj. FSS"],
        False: ["Ingresos: SPNF-SPC", "Egresos: Primarios SPNF-SPC",
                "Egresos: Inversiones SPNF-SPC",
                "Intereses: SPNF", "Egresos: Totales SPNF",
                "Resultado: Primario intendencias",
                "Resultado: Primario BSE", "Resultado: Primario SPNF",
                "Resultado: Global SPNF"]},
    "gc": {True: ["Ingresos: GC-BPS aj. FSS", "Egresos: Primarios GC-BPS",
                  "Egresos: Inversiones GC-BPS",
                  "Intereses: GC-BPS aj. FSS",
                  "Egresos: Totales GC-BPS aj. FSS",
                  "Resultado: Primario GC-BPS aj. FSS",
                  "Resultado: Global GC-BPS aj. FSS"],
           False: ["Ingresos: GC-BPS", "Egresos: Primarios GC-BPS",
                   "Egresos: Inversiones GC-BPS",
                   "Intereses: GC-BPS", "Egresos: Totales GC-BPS",
                   "Resultado: Primario GC-BPS",
                   "Resultado: Global GC-BPS"]}
}
