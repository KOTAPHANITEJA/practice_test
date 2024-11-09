from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def resume(request):
    personal_info = {
        'name': 'K.PHANI TEJA',
        'father_name': 'K.KIRAN KUMAR',
        'mother_name': 'K.RAJYA LAKSHMI',
        'school': 'NR OLYMPIAD SCHOOL',
        'university': 'KLH UNIVERSITY',
        'achievements': [
            '1st Prize in School Competitions.',
            'Participated in Robo Race Competition in University.',
            'Achieved several medals in school.'
        ],
        'address': 'SRINAGAR COLONY',
        'blood_group': 'O POSITIVE',
        'skills': [
            'Python Programming-Beginner Level',
            'Web Development-Beginner Level',
            'Data Analysis-Beginner Level',
            'Machine Learning-Beginner Level'
        ],
        'interests': [
            'Artificial Intelligence',
            'Robotics',
            'Traveling',
        ],
        'projects': [
            'Developed a Online Booking Website using Django.-"https://github.com/KOTAPHANITEJA/projectt"',
            'Developed a personal portfolio website using Django.-"https://github.com/KOTAPHANITEJA/practice_test"',
        ],
        'social_media': {
            'github': 'https://github.com/KOTAPHANITEJA',
        },
        'contact_info': {
            'email': '2310080065@klh.edu.in',
            'phone': '8341134293',
        },
        'about_me': 'I am a passionate learner and tech enthusiast with a keen interest in software development and AI. I love to explore new technologies and work on innovative projects.',
    }
    return render(request, 'resume.html', personal_info)