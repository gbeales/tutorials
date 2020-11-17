class Errors {
    constructor() {
        this.errors = {};
    }

    get(field) {
        if (this.errors[field]) {
            return this.errors[field];
        }
    }

    record(errors) {
        this.errors = errors
    }

    clear(field) {
        if (field) Vue.delete(this.errors, field);
        else this.errors = {};
    }

    has(field) {
        return this.errors.hasOwnProperty(field)
    }

    any() {
        return Object.keys(this.errors).length > 0;
    }
}

class Form {

    constructor(data) {
        this.originalData = data;

        for (let field in data) {
            this[field] = data[field];
        }

        this.errors = new Errors();
    }

    data() {
        // let data = Object.assign({}, this);
        // delete data.originalData;
        // delete data.errors;
        let data = {}

        for (let property in this.originalData) {
            data[property] = this[property]
        }

        return data
    }

    reset() {
        for (let field in this.originalData) {
            this[field] = '';
        }

        this.errors.clear()
    }

    submit(requestType, url) {      //form.submit('POST', '/some-endpoint')
        return new Promise((resolve, reject) => {
            axios[requestType](url, this.data())
                .then(response => {
                    this.onSuccess(response.data);

                    resolve(response.data);
                })
                .catch(error => {
                    this.onFail(error.response.data);

                    reject(error.response.data);
                })
        })

    }

    onSuccess(data) {
        alert(data.message);
        this.reset()
    }

    onFail(error) {
        this.errors.record(error);
    }
    
    post(url) {
        return this.submit('post', url)
    }
}


new Vue({

    el: '#root',

    data: {

        form: new Form({
            name: '',
            description: ''
        })
    },

    methods: {
        onSubmit() {
            this.form.post('/store')
            .then(data => console.log(data))
            .catch(error => console.log(error))
        }
    }

});