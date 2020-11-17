Vue.component('tabs', {
    template:`
    <div>
        <div class="tabs">
            <ul>
                <li v-for="tab in tabs" :class="{ 'is-active': tab.isActive }">
                    <a :href="tab.href" @click="selectTab(tab)">{{ tab.name }}</a>
                </li>
            </ul>
        </div>

        <div class="tabs-details">
            <slot></slot>
        </div>
    </div>
    `,

    data() {
        return {tabs: []};
    },

    created() {
        this.tabs = this.$children;
    },

    methods: {
        selectTab(selectedTab) {
            this.tabs.forEach(tab => {
                tab.isActive = (tab.name == selectedTab.name);
            })
        }
    }
})

Vue.component('tab', {
    template: `
    <div v-show="isActive"><slot></slot></div>
    `,

    props: {
        name: {required: true},
        selected: {default: false}
    },

    data() {
        return {
            isActive: false
        }
    },

    computed: {
        href() {
            return '#' + this.name.toLowerCase().replace(/ /g, '-');
        }
    },

    mounted() {
        this.isActive = this.selected;
    }
});


Vue.component('modal', {
    template:`
    <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content">
        <div class="box">
            <p>
                <slot></slot>
            </p>
        </div>
    </div>
    <button class="modal-close" aria-label="close" @click="$emit('close')">x</button>
  </div>`
});


Vue.component('message', {
    
    props: ['title', 'body'],

    data() {
        return {
            isVisible: true
        };
    },

    template: `
        <article class="message" v-show="isVisible">
                <div class="message-header">
                    {{ title }}
                <button class="delete" @click="isVisible = false" aria-label="delete"></button>
                </div>
                <div class="message-body">
                    {{ body }}
                </div>
            </article>
    `
});

new Vue({
    el: '#root',

    data: {
        showModal: false
    }
});