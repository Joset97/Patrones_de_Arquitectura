using Microsoft.AspNetCore.Mvc;
using StudentApp.Models;
using System.Collections.Generic;

namespace StudentApp.Controllers
{
    public class StudentController : Controller
    {
        private static List<Student> students = new()
        {
            new Student { Id = 1, Name = "Juan Pérez", Email = "juanSiPerez@example.com" },
            new Student { Id = 2, Name = "Paquita la del Barrio", Email = "Paquita@example.com" }
        };

        public IActionResult Index()
        {
            return View(students);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(Student student)
        {
            students.Add(student);
            return RedirectToAction("Index");
        }
    }
}
