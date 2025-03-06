using Microsoft.EntityFrameworkCore;
using StudentAPI.Interfaces;
using StudentAPI.Models;

namespace StudentAPI.Data
{
    public class StudentRepository : IStudentRepository
    {
        private readonly AppDbContext _context;

        public StudentRepository(AppDbContext context)
        {
            _context = context;
        }

        public Student GetById(int id)
        {
            return _context.Students.Find(id); // Busca al estudiante por ID en la base de datos
        }

        public void Add(Student student)
        {
            _context.Students.Add(student);
            _context.SaveChanges(); // Guarda el nuevo estudiante en la base de datos
        }
    }
}
