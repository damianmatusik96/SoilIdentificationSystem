import {Nav, Navbar} from "react-bootstrap";
import React from "react";

const TopBar = () => (
    <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#home">Navbar</Navbar.Brand>
        <Nav className="mr-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/About">About</Nav.Link>
        </Nav>
    </Navbar>
);
export default TopBar;