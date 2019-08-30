import React from "react";
import InputFiles from "react-input-files";
import {Button} from "react-bootstrap";

class SubmitComponent extends React.Component {
    // state = {
    //     file: 'file',
    //     type: this.props.type
    // };
    // onChange = (files, e) => {
    //     // e.preventDefault();// Stop form submit
    //     const formData = new FormData();
    //     formData.append('file', files[0]);
    //     console.warn("msg", formData);
    //     this.setState({file: formData});
    //     this.fileUpload(formData)
    // };
    //
    // fileUpload = (formData) => {
    //     const url = 'http://localhost:5000/save/' + this.state.type;
    //     console.log(this.state.type);
    //     return fetch(url, {method: 'POST', body: formData})
    //         .then(response => console.log(response.data));
    //
    // };

    render() {
        return (
            <InputFiles onChange={this.props.onClick}>
                <Button variant="dark"
                        style={{margin: 5}}>
                    Upload files
                </Button>
            </InputFiles>
        )
    }
}
export default SubmitComponent;