window.addEventListener("load", function (event) {
    // .. using https://github.com/Akryum/vue-observe-visibility
    new Vue({
        el: '#lazy_load',
        data: {},
        created: function () {
            this.animationListeners = {
                animation: 'animationend',
                OAnimation: 'oAnimationEnd',
                MozAnimation: 'mozAnimationEnd',
                WebkitAnimation: 'webkitAnimationEnd',
            }
        },
        methods: {

            visibilityChanged(isVisible, entry) {
                let entryIndex = this.getNodeIndex(entry.target);
                let entryAnimatedChildern = entry.target.getElementsByClassName("animated");
                let animeclass = '';
                let isEven = false;

                if (entry.isIntersecting) {
                    animeclass += 'In'
                } else {
                    if (!isVisible) {
                        animeclass += 'Out'
                        entry.target.style.visibility = 'hidden';
                    } else {
                        return
                    }
                }



                if (entryIndex % 2 == 0) {
                    isEven = true;
                }



                let i = 0;
                while (i < entryAnimatedChildern.length) {


                    for (var key in this.animationListeners) {
                        entryAnimatedChildern[i].addEventListener(this.animationListeners[key], this.removeAnimationClasses);
                    }
                    entryAnimatedChildern[i].style.visibility = 'visible';
                    i++;
                }

                let animeCLassStatic = animeclass;
                animeclass = 'bounce' + animeclass;
                animeCLassStatic = 'fade' + animeCLassStatic;
                let xr = 0;
                if (isEven) {
                    animeclass += 'Left';
                    xr = 1
                } else {
                    animeclass += 'Right';
                }


                entryAnimatedChildern[1 - xr].classList.add(animeclass);
                entryAnimatedChildern[xr].classList.add(animeCLassStatic);
            },
            removeAnimationClasses(event) {
                for (var key in this.animationListeners) {
                    event.target.removeEventListener(this.animationListeners[key], this.removeAnimationClasses);
                };
                event.target.classList.remove(event.animationName);


            },
            getNodeIndex(node) {
                var index = 0;
                while ((node = node.previousSibling)) {
                    if (node.nodeType != 3 || !/^\s*$/.test(node.data)) {
                        index++;
                    }
                }
                return index;
            }
        },
    })
});
<HTML example>
    <div id="lazy_load">
        <section id="xx">
                <aside id="topH">
                        <div class="ovrl abso"></div>
                        <div class="bg abso"></div>
                        <div class="sloupec">
                                <div class="topText">
                                        <h1>xxx</h1>
                                </div>
                        </div>
                </aside>
                <aside id="mainC" class="cont">
                        <div v-observe-visibility="visibilityChanged" class="contactRow cols fboxAuto spaceb vCntr">
                                <div class="sstmdoL imgcol animated">
                                         <img src="images/img.jpg">
                                </div>
                                <div class="sstmdoR">
                                        <div class="txcol animated">
                                                <p>bla</p>
                                        </div>
                                </div>
                        </div>
                        <div v-observe-visibility="visibilityChanged" class="contactRow cols fboxAuto spaceb vCntr">
                                <div class="sstmdoL">
                                        <div class="txcol animated">
                                               <p>bla</p>
                                        </div>
                                </div>
                                <div class="sstmdoR imgcol animated">
                                        <img src="images/img.jpg">
                                </div>
                        </div>
                        <div v-observe-visibility="visibilityChanged" class="contactRow cols fboxAuto spaceb vCntr">
                                <div class="sstmdoL imgcol animated">
                                        <img src="images/img.jpg">
                                </div>
                                <div class="sstmdoR">
                                        <div class="txcol animated">
                                                <p>bla</p>
                                        </div>
                                </div>
                        </div>
                </aside>
        </section>
</div>
</html>
<CSS EXAMPLE>
    #lazy_load {
	overflow: hidden;
}

.animated {
	visibility: hidden;
}
 .imgcol.animated {
	 animation-delay: .4s;
		animation-duration: .4s;
} 

.txcol.animated {
	animation-duration: 1s;
} 
    </CSS>
