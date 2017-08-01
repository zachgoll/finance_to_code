// all middleware
var middlewareObj = {};
var Campground = require("../models/campground");
var Comment = require("../models/comment");

middlewareObj.checkCampgroundOwnership = function(req, res, next){
    if(req.isAuthenticated()){
        Campground.findById(req.params.id, function(err, foundCampground){
        if(err){
            req.flash("error_messages", "Unable to find Campground");
            res.redirect("back");
        } else{
            if(foundCampground.author.id.equals(req.user._id)){
               next();
            } else {
                req.flash("error_messages", "You do not have permission to edit");
                res.redirect('back');
            }
        }
    });
    } else {
        req.flash("error_messages", "Please login first!");
        res.redirect("back");
    }
}


middlewareObj.checkCommentOwnership = function(req, res, next){
    if(req.isAuthenticated()){
        Comment.findById(req.params.comment_id, function(err, foundComment){
        if(err){
            req.flash("error_messages", "Unable to find Comment");
            res.redirect("back");
        } else{
            if(foundComment.author.id.equals(req.user._id)){
               next();
            } else {
                req.flash("error_messages", "You do not have permission to edit");
                res.redirect('back');
            }
        }
    });
    } else {
        req.flash("error_messages", "Please login first!");
        res.redirect("back");
    }
}

middlewareObj.isLoggedIn = function(req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    req.flash("error_messages", "Please login first!");
    res.redirect("/login");
}

module.exports = middlewareObj;