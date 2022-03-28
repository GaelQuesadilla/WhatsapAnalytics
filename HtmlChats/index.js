class View {
    constructor() {
        this.indexSelector = document.querySelector("#indexSelector");
        this.indexButton = document.querySelector("#indexReturnButton");

        this.indexButton.addEventListener("click", () => {
            this.returnPage();
        });
    }

    returnPage() {
        const value = this.indexSelector.value;
        let ref = window.location.pathname;

        const fileName = this.get_last_value(ref, "/");

        const fileNumber = this.get_last_value(fileName, "-").replace(
            ".html",
            ""
        );
        const newFile = fileName.replace(fileNumber, `-${value}`);

        const location = window.location;
        location.pathname = location.pathname.replace(fileName, newFile)
        console.log(location)
        
    }

    get_last_value(element, separator) {
        let index = -1;

        for (let value in element) {
            if (element[value] === separator) {
                index = value;
            }
        }

        if (index === -1) {
            console.error("ERROR: SEPARATOR NOT FOUNDED");
            return null;
        } else {
            let result = element.substr(index, element.length);
            return result;
        }
    }
}

const view = new View();
