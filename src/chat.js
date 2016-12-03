var app = angular.module('chatDisplay',[]);

app.controller('chatCtrl', function($scope) {
	$scope.records = [];
	$scope.addChat = function(message) {
		$scope.records.push(message);
		$scope.$apply();
	};
});
