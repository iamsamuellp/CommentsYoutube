import React, {useState}  from 'react';






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
                <button className="SearchButton" type='submit' value="search">Submit</button>
            </form>
        
        </div>
    );
}

export default Search;