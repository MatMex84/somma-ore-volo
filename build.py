"""Genera index.html (file unico e autonomo) incorporando pdf.js in src/template.html.
Uso: npm install && python3 build.py
"""
def js(p):
    return open(p, encoding='utf-8').read().replace('</script', '<\\/script')

t = open('src/template.html', encoding='utf-8').read()
t = t.replace('/*PDFJS*/', js('node_modules/pdfjs-dist/build/pdf.min.js'))
t = t.replace('/*WORKER*/', js('node_modules/pdfjs-dist/build/pdf.worker.min.js'))
open('index.html', 'w', encoding='utf-8').write(t)
