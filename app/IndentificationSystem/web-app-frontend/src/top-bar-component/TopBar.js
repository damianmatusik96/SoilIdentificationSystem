import {Button, Nav, Navbar} from "react-bootstrap";
import React from "react";
import {Link} from "react-router-dom";

const TopBar = () => (
    <Navbar bg="dark" variant="dark">
        <Nav className="mr-auto">
            <Link to='/'>
                <Button variant='dark'>
                    Home
                </Button>
            </Link>
            <Link to='/get-started'>
                <Button variant='dark'>
                    Get started
                </Button>
            </Link>
        </Nav>
    </Navbar>
);
export default TopBar;