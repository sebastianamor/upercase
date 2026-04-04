// Diccionario de traducciones
const traducciones = {
    es: {
        title: "🔄 Convertidor a Mayúsculas",
        subtitle: "Escribe tu texto y presiónalo para convertirlo a MAYÚSCULAS",
        label_original: "📝 Texto original:",
        placeholder: "Escribe tu texto aquí...",
        btn_convert: "🔠 Convertir a MAYÚSCULAS",
        btn_clear: "🗑️ Limpiar",
        result_title: "✨ Resultado en MAYÚSCULAS:",
        btn_copy: "📋 Copiar",
        empty_result: "El resultado aparecerá aquí...",
        copied: "✅ ¡Texto copiado!",
        no_text: "⚠️ No hay texto para copiar"
    },
    en: {
        title: "🔄 Uppercase Converter",
        subtitle: "Write your text and press to convert to UPPERCASE",
        label_original: "📝 Original text:",
        placeholder: "Write your text here...",
        btn_convert: "🔠 Convert to UPPERCASE",
        btn_clear: "🗑️ Clear",
        result_title: "✨ Result in UPPERCASE:",
        btn_copy: "📋 Copy",
        empty_result: "The result will appear here...",
        copied: "✅ Text copied!",
        no_text: "⚠️ No text to copy"
    },
    zh: {
        title: "🔄 大写转换器",
        subtitle: "输入文本并按回车键转换为大写",
        label_original: "📝 原始文本：",
        placeholder: "在这里输入您的文本...",
        btn_convert: "🔠 转换为大写",
        btn_clear: "🗑️ 清除",
        result_title: "✨ 大写结果：",
        btn_copy: "📋 复制",
        empty_result: "结果将显示在这里...",
        copied: "✅ 文本已复制！",
        no_text: "⚠️ 没有要复制的文本"
    },
    ja: {
        title: "🔄 大文字コンバーター",
        subtitle: "テキストを入力してEnterキーを押すと大文字に変換されます",
        label_original: "📝 元のテキスト：",
        placeholder: "ここにテキストを入力...",
        btn_convert: "🔠 大文字に変換",
        btn_clear: "🗑️ クリア",
        result_title: "✨ 大文字の結果：",
        btn_copy: "📋 コピー",
        empty_result: "結果がここに表示されます...",
        copied: "✅ テキストをコピーしました！",
        no_text: "⚠️ コピーするテキストがありません"
    }
};

let idiomaActual = 'es';

// Función para cambiar idioma
async function cambiarIdioma(idioma) {
    idiomaActual = idioma;
    
    // Guardar en el servidor
    try {
        await fetch('/cambiar-idioma', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ idioma: idioma })
        });
    } catch (error) {
        console.error('Error al guardar idioma:', error);
    }
    
    // Actualizar textos en la página
    actualizarTextos(idioma);
    
    // Actualizar clase activa en botones
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('data-lang') === idioma) {
            btn.classList.add('active');
        }
    });
}

// Función para actualizar todos los textos
function actualizarTextos(idioma) {
    const texts = traducciones[idioma];
    if (!texts) return;
    
    document.getElementById('title').textContent = texts.title;
    document.getElementById('subtitle').textContent = texts.subtitle;
    document.getElementById('label-original').textContent = texts.label_original;
    document.getElementById('btn-convert').innerHTML = texts.btn_convert;
    document.getElementById('btn-clear').innerHTML = texts.btn_clear;
    document.getElementById('result-title').textContent = texts.result_title;
    document.getElementById('btn-copy').innerHTML = texts.btn_copy;
    
    const textarea = document.getElementById('texto');
    if (textarea.getAttribute('data-placeholder-original') === null) {
        textarea.setAttribute('data-placeholder-original', textarea.placeholder);
    }
    textarea.placeholder = texts.placeholder;
    
    const resultadoDiv = document.getElementById('resultado');
    const emptyMessages = {
        es: "El resultado aparecerá aquí...",
        en: "The result will appear here...",
        zh: "结果将显示在这里...",
        ja: "結果がここに表示されます..."
    };
    
    if (resultadoDiv.textContent === "" || 
        resultadoDiv.textContent === "El resultado aparecerá aquí..." || 
        resultadoDiv.textContent === "The result will appear here..." ||
        resultadoDiv.textContent === "结果将显示在这里..." ||
        resultadoDiv.textContent === "結果がここに表示されます...") {
        resultadoDiv.textContent = texts.empty_result;
    }
}

// Convertir en tiempo real
const textarea = document.getElementById('texto');
const resultadoDiv = document.getElementById('resultado');

function convertirEnTiempoReal() {
    const texto = textarea.value;
    const emptyMessages = {
        es: "El resultado aparecerá aquí...",
        en: "The result will appear here...",
        zh: "结果将显示在这里...",
        ja: "結果がここに表示されます..."
    };
    resultadoDiv.textContent = texto.toUpperCase() || emptyMessages[idiomaActual];
}

textarea.addEventListener('input', convertirEnTiempoReal);

textarea.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        convertirEnTiempoReal();
    }
});

function limpiarTexto() {
    textarea.value = '';
    const emptyMessages = {
        es: "El resultado aparecerá aquí...",
        en: "The result will appear here...",
        zh: "结果将显示在这里...",
        ja: "結果がここに表示されます..."
    };
    resultadoDiv.textContent = emptyMessages[idiomaActual];
    textarea.focus();
}

async function copiarTexto() {
    const textoACopiar = resultadoDiv.textContent;
    const emptyMessages = {
        es: "El resultado aparecerá aquí...",
        en: "The result will appear here...",
        zh: "结果将显示在这里...",
        ja: "結果がここに表示されます..."
    };
    
    if (textoACopiar && textoACopiar !== emptyMessages[idiomaActual]) {
        try {
            await navigator.clipboard.writeText(textoACopiar);
            mostrarToast(traducciones[idiomaActual].copied, '#28a745');
        } catch (err) {
            // Fallback para navegadores antiguos
            const textareaTemp = document.createElement('textarea');
            textareaTemp.value = textoACopiar;
            document.body.appendChild(textareaTemp);
            textareaTemp.select();
            document.execCommand('copy');
            document.body.removeChild(textareaTemp);
            mostrarToast(traducciones[idiomaActual].copied, '#28a745');
        }
    } else {
        mostrarToast(traducciones[idiomaActual].no_text, '#ff9800');
    }
}

function mostrarToast(mensaje, color = '#333') {
    const toast = document.getElementById('toast');
    toast.textContent = mensaje;
    toast.style.backgroundColor = color;
    toast.className = "toast show";
    
    setTimeout(() => {
        toast.className = "toast";
    }, 2000);
}

// Prevenir envío del formulario
document.getElementById('converterForm').addEventListener('submit', function(e) {
    e.preventDefault();
    convertirEnTiempoReal();
});

// Inicializar si hay texto cargado
if (textarea.value) {
    convertirEnTiempoReal();
}

// Marcar el botón del idioma actual como activo
document.addEventListener('DOMContentLoaded', function() {
    // Obtener idioma de la sesión (desde Flask)
    const idiomaServidor = '{{ idioma }}';
    idiomaActual = idiomaServidor;
    
    const botonActivo = document.querySelector(`.lang-btn[data-lang="${idiomaActual}"]`);
    if (botonActivo) {
        botonActivo.classList.add('active');
    }
    actualizarTextos(idiomaActual);
});