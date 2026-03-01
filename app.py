print("=== НАЧАЛО ВЫПОЛНЕНИЯ ===")
import sys
print("Версия Python:", sys.version)
print("Текущий путь:", sys.path[0])

from flask import Flask, render_template, request


app = Flask(__name__)

# Данные о учебных заведениях
EDU_INSTITUTIONS = {
    "9": [
        {
            "city": "Ярославль",
            "name": "Ярославский градостроительный колледж",
            "specialties": ["Архитектура", "Строительство и эксплуатация зданий", "Дизайн"],
            "entrance": "Конкурс аттестатов (средний балл)",
            "required_subjects": ["Русский язык", "Математика"],
            "link": "https://yargradkol.edu.yar.ru"
        },
        {
            "city": "Ярославль",
            "name": "Ярославский колледж сервиса и дизайна",
            "specialties": ["Дизайн", "Технологии индустрии красоты", "Швейное производство"],
            "entrance": "Конкурс аттестатов",
            "required_subjects": ["Русский язык", "Математика"],
            "link": "https://yksid.edu.yar.ru"
        },
        {
            "city": "Рыбинск",
            "name": "Рыбинский полиграфический колледж",
            "specialties": ["Полиграфическое производство", "Дизайн", "Реклама"],
            "entrance": "Конкурс аттестатов",
            "required_subjects": ["Русский язык", "Математика"],
            "link": "https://rpk.rybinsksu.ru"
        },
        {
            "city": "Кострома",
            "name": "Костромской торгово-экономический колледж",
            "specialties": ["Гостиничное дело", "Товароведение", "Банковское дело"],
            "entrance": "Конкурс аттестатов",
            "required_subjects": ["Русский язык", "Математика"],
            "link": "https://ktek44.ru"
        }
    ],
    "11": [
        {
            "city": "Ярославль",
            "name": "ЯрГУ им. П. Г. Демидова",
            "specialties": ["Прикладная математика и информатика", "Юриспруденция", "Психология"],
            "entrance": "ЕГЭ",
            "required_subjects": ["Русский язык", "Математика (проф.)", "Информатика / Обществознание"],
            "min_scores": "От 50–60 баллов по каждому предмету",
            "link": "https://uniyar.ac.ru"
        },
        {
            "city": "Ярославль",
            "name": "ЯГТУ",
            "specialties": ["Строительство", "Машиностроение", "Информационные системы"],
            "entrance": "ЕГЭ",
            "required_subjects": ["Русский язык", "Математика (проф.)", "Физика / Информатика"],
            "min_scores": "От 45–55 баллов по каждому предмету",
            "link": "https://ystu.ru"
        },
        {
            "city": "Рыбинск",
            "name": "РГАТУ им. П. А. Соловьёва",
            "specialties": ["Авиастроение", "Автоматизация технологических процессов", "Экономика"],
            "entrance": "ЕГЭ",
            "required_subjects": ["Русский язык", "Математика (проф.)", "Физика / Обществознание"],
            "min_scores": "От 48–52 баллов по каждому предмету",
            "link": "https://rsatu.ru"
        },
        {
            "city": "Кострома",
            "name": "КГУ им. Н. А. Некрасова",
            "specialties": ["Педагогика", "Филология", "Биология"],
            "entrance": "ЕГЭ",
            "required_subjects": ["Русский язык", "Математика (баз./проф.)", "Обществознание / Биология"],
            "min_scores": "От 45–50 баллов по каждому предмету",
            "link": "https://ksu.edu.ru"
        }
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_class = request.form.get('class', '9')  # По умолчанию — 9 класс
    institutions = EDU_INSTITUTIONS.get(selected_class, [])
    return render_template('index.html', institutions=institutions, selected_class=selected_class)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
print("\n=== СЕРВЕР ЗАПУЩЕН ===")
print("Откройте в браузере: http://127.0.0.1:5000")
if __name__ == '__main__':
    app.run(debug=True)

print("\nНажмите Enter для остановки...")
name = os.environ.get(GaraX, Томас)

print(f"привет,{Garax}!")


