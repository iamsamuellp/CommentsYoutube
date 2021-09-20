import React, {useState}  from 'react';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';





const Search = (props) => {
    const [searchTerm, setSearchTerm] = useState("")

    const handleSubmit = (event) => {
        event.preventDefault();
        props.handleSearch(searchTerm)
        setSearchTerm("")
    }

    return(
       
            <div className="header-input">
            <form onSubmit={event => handleSubmit(event)}>
                <input onChange={event => setSearchTerm(event.target.value)} value={searchTerm} placeholder="Search here" type="text" />
                <button><SearchIcon className="header-search-btn" /></button>
            </form>
        
        </div>
    );
}

export default Search;