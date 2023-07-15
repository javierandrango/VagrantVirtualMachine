//catch filter by event
function filterContent(){
    // one single value of all options: [All,course1,course2,...]
    var filterBy = document.getElementById("filter-by").value;
    
    // HTML colection (every <article class='course'>)
    var articleCourses = document.getElementsByClassName("course");

    // Hide all
    for (var i=0; i<articleCourses.length; i++){
        articleCourses[i].style.display = "none";
    }
    
    // Show selected option
    if(filterBy == 'All'){
        for (var i=0; i<articleCourses.length; i++){
            articleCourses[i].style.display = "block";
        }
    }
    else{
        var course = document.getElementsByClassName(filterBy);
        //console.log(course[0])
        // course[i] access <article> inside the collection
        for (var i=0; i<course.length;i++){
            course[i].style.display = "block";
        }
        
    }
    
}
