import React from 'react';
import request from 'superagent';

export default class VehicleImages extends React.Component {
	constructor(){
		super();
		this.state = {
			AvailableServicesImagesArray: [],
			AvailableServicesImagesHash : {}
		}
	}
	getImagesData() {

		var url="/listavailableserviceimages";
		var x = this;
		request.get(url).then((imageresponse) => {
			console.log("listavailableserviceimages imageresponse:",
				JSON.stringify(imageresponse.body));
			var tempvtid;
			var tempstid;
			var tempBeforeCleanImage;
			var tempAfterCleanImage;

			var tempArray = imageresponse.body;
	  	var tempAvailableServiceImagesHash = {};

			if(tempArray) {
				for(var i = 0; i < tempArray.length ; i++ ) {
					tempvtid = tempArray[i].vehicle_type_id;
					tempstid = tempArray[i].service_type_id;
					tempBeforeCleanImage = tempArray[i].before_clean_image;
					tempAfterCleanImage = tempArray[i].after_clean_image;

					if (tempvtid in tempAvailableServiceImagesHash == false) {
						console.log("Hash doesn't contain tempvtid:"+tempvtid);
						tempAvailableServiceImagesHash[tempvtid] = []; 
					}

					if (tempstid in tempAvailableServiceImagesHash[tempvtid] == false) {
						console.log("Hash doesn't contain tempstid:"+tempstid);
						tempAvailableServiceImagesHash[tempvtid][tempstid] = []; //{};
					}
					
					tempAvailableServiceImagesHash[tempvtid][tempstid]['before_clean_file'] = '';
					tempAvailableServiceImagesHash[tempvtid][tempstid]['before_clean_image'] = tempBeforeCleanImage;
					tempAvailableServiceImagesHash[tempvtid][tempstid]['after_clean_image'] = tempAfterCleanImage;
				} // end of - for(var i = 0; i < tempArray.le
			} // end of - if(tempArray) {

			console.log("tempAvailableServiceImagesHash:"+tempAvailableServiceImagesHash)
			var newState = x.state;
			newState["AvailableServicesImagesArray"] = tempArray;
			newState["AvailableServicesImagesHash"] = tempAvailableServiceImagesHash;
			x.setState(newState);						

		});

	} // end of - getImagesData
	componentWillMount() {
		this.getImagesData();
	} 

	render(){
		return(
			<div>
				{
					this.state.AvailableServicesImagesArray.map((images,index) =>(
						<div key={index} className="col-md-3">
							<img src={images["after_clean_image"]}  height="40" width="40" />
						</div>
						))
				}
			</div>
		)
	}
		
}