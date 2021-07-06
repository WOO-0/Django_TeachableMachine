window.onload = function(){
    let Hidden = (target) => {
        target.style.display = 'none';
        let subtarget = document.getElementById("menu-holder");
        subtarget.style.borderRadius = '0 10px 10px 10px'
    }
    let Open = (target) => {
        target.style.display = 'block';
        let subtarget = document.getElementById("menu-holder");
        subtarget.style.borderRadius = '0 10px 0 0'
    }
    let Open_Hidden = (target) => {
        if (window.getComputedStyle(target).display === 'none'){
            return Open(target);
        }else{
            return Hidden(target);
        }
    }

    let targetId = document.getElementById('main-menu');
    let slideBtnClick = (cl,sl) =>{
        document.querySelector(cl).addEventListener('click', () => sl(targetId));
    }
    slideBtnClick('.collapsed', Open_Hidden);
}