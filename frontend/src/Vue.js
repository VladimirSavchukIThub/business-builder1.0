data() {
    return {
        configurations: [],
    };
},
methods: {
    async fetchConfigurations() {
        const response = await fetch('http://localhost:5000/business_configurations');
        this.configurations = await response.json();
    },
},
created() {
    this.fetchConfigurations();
}
