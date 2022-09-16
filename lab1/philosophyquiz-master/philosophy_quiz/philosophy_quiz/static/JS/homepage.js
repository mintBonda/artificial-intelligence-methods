"use strict";

window.addEventListener('DOMContentLoaded', function()
{
    const   menuButton      = document.querySelector('.menu-button'),
            menuPanel       = document.querySelector('.menu'),
            gridItems       = document.querySelectorAll('#philosophers .grid .item'),
            startButton     = document.querySelector('#quiz'),
            ratingsButton   = document.querySelector('#ratings'),
            darkscreen      = document.querySelector('.darkscreen'),
            modal           = darkscreen.querySelector('.modal'),
            modalImg        = modal.querySelector('img'),
            modalText       = modal.querySelector('span.info'),
            pool            = document.querySelector('.pool');

    menuButton.addEventListener('click', function()
    {
        const   l1 = this.querySelector('.line1'),
                l2 = this.querySelector('.line2'),
                l3 = this.querySelector('.line3');

        if (this.dataset.state == 'on')
        {
            l1.style.transform = 'none';
            l2.style.visibility = 'visible';
            l3.style.transform = 'none';

            menuPanel.style.transform = 'translateX(-100%)';

            this.dataset.state = 'off';
        }
        else if (this.dataset.state == 'off')
        {
            l1.style.transform = 'rotate(43deg)';
            l2.style.visibility = 'hidden';
            l3.style.transform = 'rotate(-43deg)';

            menuPanel.style.transform = 'none';

            this.dataset.state = 'on';
        }
    });

    let n = 0;
    for (const item of gridItems)
    {
        item.dataset.n = n++;
        item.addEventListener('click', function()
        {
            if (darkscreen.dataset.state == 'off')
            {
                darkscreen.style.display = 'flex';
                modalImg.src = pool.querySelectorAll('img')[this.dataset.n].src;
                modalText.textContent = pool.querySelectorAll('span')[this.dataset.n].textContent;
            }
            else if (darkscreen.dataset.state == 'on')
            {
                darkscreen.style.display = 'none';
            }
        });
    }

    darkscreen.addEventListener('click', function(e)
    {
        if (e.target == this)
            darkscreen.style.display = 'none';
    })

    startButton.addEventListener('click', function()
    {
        //redirect to the gate
        window.location.replace('../gate/');
    });

    ratingsButton.addEventListener('click', function()
    {
        //redirect to the leaderboard
        window.location.replace('../quiz/leaderboard/');
    });
});