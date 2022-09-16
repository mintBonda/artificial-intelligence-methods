"use strict";
const c = console.log;

document.addEventListener('DOMContentLoaded', function()
{
    let timer       = document.querySelector('.timer'),
        initialTime = 15 * 60 * 1000, //in ms
        varTime     = initialTime,
        killTimer;
    startTimer();

    let mainForm        = document.forms['main-form'],
        finishButton    = mainForm.querySelector('input[type="submit"]'),
        cancelButton    = mainForm.querySelector('input[value="Выйти"]');
    finishButton.addEventListener('click', function(e)
    {
        e.preventDefault();
        showConfirmBox('Вы действительно хотите завершить выполнение?', processSubmission);
    });
    cancelButton.addEventListener('click', function()
    {
        showConfirmBox('Вы действительно хотите выйти?', function()
        {
            //redirect to the homepage
            window.location.replace('/');
        });
    });

    function startTimer()
    {
        let minutes = timer.querySelector('span.minutes'),
            seconds = timer.querySelector('span.seconds'),
            mark    = Date.now();

        killTimer = setTimeout(function loop()
        {
            killTimer = setTimeout(loop, 100);
            varTime -= Date.now() - mark;
            if (varTime <= 0)
            {
                clearTimeout(killTimer);
                minutes.textContent = seconds.textContent = '00';

                showAlertBox('Время вышло, Вы будете перенаправлены на страницу с результатами', processSubmission)
            }
            else
            {
                minutes.textContent = String((Math.round(varTime / 1000) - Math.round(varTime / 1000) % 60) / 60).padStart(2, '0');
                seconds.textContent = String(Math.round(varTime / 1000) % 60).padStart(2, '0');
                mark = Date.now();
            }
        }, 100);
    }

    function processSubmission()
    {
        clearTimeout(killTimer);

        let timeInput = mainForm.time,
        timeString = String((Math.round((initialTime - varTime) / 1000) - Math.round((initialTime - varTime) / 1000) % 60) / 60) + ':' + String(Math.round((initialTime - varTime) / 1000) % 60);


        timeInput.setAttribute('value', timeString);

        mainForm.submit();
    }

    function showTextBox(message = '')
    {
        let darkScreen      = document.querySelector('.modal-darkscreen'),
            textBox         = darkScreen.querySelector('.modal-window.plain-text'),
            textBoxMessage  = textBox.querySelector('.message');

        textBoxMessage.textContent = message;
        textBox.style.display = 'block';
        darkScreen.style.display = 'flex';

        darkScreen.addEventListener('click', function (e)
        {
            if (e.target == this)
            {
                textBoxMessage.textContent = '';
                textBox.style.display = 'none';
                darkScreen.style.display = 'none';
            }
        });
    }

    function showAlertBox(message = '', callback = Math.abs)
    {
        let darkScreen      = document.querySelector('.modal-darkscreen'),
            alertBox        = darkScreen.querySelector('.modal-window.alert-box'),
            alertBoxMessage = alertBox.querySelector('.message'),
            alertBoxButton  = alertBox.querySelector('input[type="button"]');

        if (darkScreen.style.display != 'none')
        {
            for (let modal of darkScreen.querySelectorAll('.modal-window'))
            {
                modal.style.display = 'none';
            }
        }

        alertBoxMessage.textContent = message;
        alertBox.style.display = 'block';
        darkScreen.style.display = 'flex';

        alertBoxButton.addEventListener('click', function()
        {
            alertBoxMessage.textContent = '';
            alertBox.style.display = 'none';
            darkScreen.style.display = 'none';
            callback();
        }, {once: true});
    }

    function showConfirmBox(message = '', yesCallback = Math.abs, noCallback = Math.abs)
    {
        let darkScreen          = document.querySelector('.modal-darkscreen'),
            confirmBox          = darkScreen.querySelector('.modal-window.confirm-box'),
            confirmBoxMessage   = confirmBox.querySelector('.message'),
            confirmBoxYesButton = confirmBox.querySelector('input[value="Да"]'),
            confirmBoxNoButton  = confirmBox.querySelector('input[value="Нет"]');

        confirmBoxMessage.textContent = message;
        confirmBox.style.display = 'block';
        darkScreen.style.display = 'flex';

        confirmBoxYesButton.addEventListener('click', function()
        {
            confirmBoxMessage.textContent = '';
            confirmBox.style.display = 'none';
            darkScreen.style.display = 'none';
            yesCallback();
            noCallback = Math.abs;
            confirmBoxNoButton.dispatchEvent(new Event('click'));
        }, {once: true});

        confirmBoxNoButton.addEventListener('click', function()
        {
            confirmBoxMessage.textContent = '';
            confirmBox.style.display = 'none';
            darkScreen.style.display = 'none';
            noCallback();
            yesCallback = Math.abs;
            confirmBoxYesButton.dispatchEvent(new Event('click'));
        }, {once: true});
    }
});

