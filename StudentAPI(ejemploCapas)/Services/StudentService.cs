using StudentAPI.Interfaces;
using StudentAPI.Models;

namespace StudentAPI.Services
{
    public class StudentService : IStudentService
    {
        private readonly IStudentRepository _studentRepository;

        public StudentService(IStudentRepository studentRepository)
        {
            _studentRepository = studentRepository;
        }

        public Student GetStudentById(int id)
        {
            return _studentRepository.GetById(id); // Delegamos la consulta a la Capa de Acceso a Datos
        }

        public void AddStudent(Student student)
        {
            _studentRepository.Add(student); // Delegamos la creación a la Capa de Acceso a Datos
        }
    }
}
