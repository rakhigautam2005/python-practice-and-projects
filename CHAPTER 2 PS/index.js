const server =  http.createserver((req,res))
{
    if(req.url ==='/about'){
        FileSystem.readfile("/about.html")
    }
}