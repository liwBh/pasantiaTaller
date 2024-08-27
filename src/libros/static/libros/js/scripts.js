// Función para ajustar la altura mínima del contenedor
function ajustarAlturaContenedor() {
    // Obtener los elementos por su ID
    const navbar = document.getElementById('navbar');
    const footer = document.getElementById('footer');
    const content = document.getElementById('content');

    // Calcular la altura del navbar y del footer
    const alturaNavbar = navbar.offsetHeight;
    const alturaFooter = footer.offsetHeight;

    // Calcular la altura restante
    const alturaRestante = window.innerHeight - (alturaNavbar + alturaFooter + 8 );
    //console.log(alturaRestante)
    //console.log(window.innerHeight )

    // Aplicar la altura mínima al contenedor
    content.style.minHeight = `${alturaRestante}px`;
}

// Ejecutar la función al cargar la página
window.addEventListener('load', ajustarAlturaContenedor);

// Volver a ejecutar la función si se redimensiona la ventana
window.addEventListener('resize', ajustarAlturaContenedor);