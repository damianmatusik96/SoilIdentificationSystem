import {Nav, Navbar} from "react-bootstrap";
import React from "react";

const TopBar = () => (
    <Navbar bg="dark" variant="dark">
        <Nav className="mr-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/get-started">Get started</Nav.Link>
        </Nav>
    </Navbar>
);
export default TopBar;