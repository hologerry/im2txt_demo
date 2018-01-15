var myApp = angular.module("FrontendApp", ['ngResource']);

myApp.config(function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.controller('MainCtrl', function ($scope, Images)
{
    console.log('In main control');

    $scope.newImage = {};

    $scope.images = Images.query();

    $scope.uploadImage = function () {
        console.log("Upload image called");
        Images.save($scope.newImage).$promise.then(
            function(response) {
                // the response is a valid image, put it at the front of the images array
                $scope.images.unshift(response);

                // reset newImage
                $scope.newImage = {};

                // toaster.pop('success', "Image uploaded!");
            }
        );
    }

    $scope.deleteImage = function (image) {
        image.$delete(
            function (response) {
                $scope.images = Images.query();
            }
        );
    }
});

myApp.directive('filesModel', filesModelDirective);
