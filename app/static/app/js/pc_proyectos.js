const buttons = document.querySelectorAll(".filter-btn");
    const projects = document.querySelectorAll(".project");

    buttons.forEach(btn => {
      btn.addEventListener("click", () => {
        const filter = btn.getAttribute("data-filter");

        // reset estilos botones
        buttons.forEach(b => {
          b.classList.remove("bg-green-500", "text-white", "font-semibold", "scale-105");
          b.classList.add("bg-white", "text-gray-600", "border-gray-300", "scale-100");
        });

        // aplicar estilo y animación al seleccionado
        btn.classList.add("bg-green-500", "text-white", "font-semibold", "scale-105");
        btn.classList.remove("bg-white", "text-gray-600");

        // filtrar proyectos con animación
        projects.forEach(project => {
          if (filter === "all" || project.getAttribute("data-category") === filter) {
            project.classList.remove("opacity-0", "scale-95", "hidden");
            setTimeout(() => {
              project.classList.add("opacity-100", "scale-100");
            }, 50);
          } else {
            project.classList.remove("opacity-100", "scale-100");
            project.classList.add("opacity-0", "scale-95");
            setTimeout(() => {
              project.classList.add("hidden");
            }, 400);
          }
        });
      });
    });