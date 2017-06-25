import React from 'react';
import request from 'superagent';
import { DropdownButton,MenuItem } from 'react-bootstrap';

export default class Price extends React.Component {
	constructor(){
		super();
		console.log("Price constructor begin");
		this.state = {
			V_T_Hash : {},
			V_T_Array : [],
			S_T_Hash : {},
			S_T_Array : [],
			V_C_Hash : {},
			V_C_Array : [],
			ASVId_Array : [],
			A_S_Hash : {},
			affectedVehicleTypeId:undefined,
			affectedServiceTypesId:undefined,
			affectedVehicleConditionId:undefined,
		};


		this.getVehicleTypesData =
			this.getVehicleTypesData.bind(this);
		this.getServiceTypesData = 
			this.getServiceTypesData.bind(this);
		this.getVehicleConditionData = 
			this.getVehicleConditionData.bind(this);
		this.getImagesData = 
			this.getImagesData.bind(this);
		this.getAvailableServiceData = 
			this.getAvailableServiceData.bind(this);

		console.log("Price constructor end");
	} // end of constructor


	getVehicleTypesData() {
		var url="/listvehicletypes";
		var x = this;
		console.log("inside getVehicleTypesData");
		request.get(url).then((vtresponse) => {
			console.log("listvehicletypes vtresponse:",JSON.stringify(vtresponse.body));
			var tempVehicleTypes = {}
			vtresponse.body.map((vehicles, index) => (
				tempVehicleTypes[vehicles.id] = {
					type:vehicles.type,
					display_text:vehicles.display_text
				}
			))
			console.log("tempVehicleTypes:"+JSON.stringify(tempVehicleTypes))
			x.setState({
				V_T_Hash : tempVehicleTypes,
				V_T_Array : vtresponse.body
			})
		});

	} // end of - getVehicleTypesData

	getServiceTypesData() {
		var url="/listservicetypes";
		var x = this;
		request.get(url).then((stresponse) => {
			console.log("listservicetypes stresponse:",JSON.stringify(stresponse.body));
			var tempServiceTypes = {}
			stresponse.body.map((services, index) => (
				tempServiceTypes[services.id] = {
					name:services.name,
					display_name:services.display_name,
					description:services.description
				}
			));

			console.log("tempServiceTypes:"+JSON.stringify(tempServiceTypes))
			x.setState({
				S_T_Hash : tempServiceTypes,
				S_T_Array : stresponse.body					
			})
		});

	} // end of - getServiceTypesData

	getVehicleConditionData() {

		var url="/listvehiclecondition";
		var x = this;
		request.get(url).then((vcresponse) => {
			console.log("listvehiclecondition vcresponse:",JSON.stringify(vcresponse.body));
			var temp_V_C_info = {}
			vcresponse.body.map((services, index) => (
				temp_V_C_info[services.id] = {
					id : services.id,								
					condition:services.condition
				}
			))

			x.setState({		
				V_C_Hash : temp_V_C_info,		
				V_C_Array : vcresponse.body
			})
		});

	} // end of - getVehicleConditionData

	getAvailableServiceData() {
		var url="/listavailableservices";
		var x = this;
		request.get(url).then((asresponse) => {
			console.log("listavailableservices asresponse:",JSON.stringify(asresponse.body));
			var tempvtid;
			var tempstid;
			var tempvcid;
			var tempbaseprice;
			var tempArray = asresponse.body;
			console.log("asresponse.body",asresponse.body);
	  	var tempA_S_Hash = {};
	  	var tempASVehiclesHash = {};
	  	var serviceypeExists;
	  	var tempLength;
	  	var tempASVId_Array = [];

			if(tempArray) {
				for(var i = 0; i < tempArray.length ; i++ ) {
					tempvtid = tempArray[i].vehicle_type_id;
					if (!tempASVId_Array.includes(tempvtid)) {
						tempASVId_Array.push(tempvtid);
					}
					tempstid = tempArray[i].service_type_id;
					tempvcid = tempArray[i].vehicle_condition_id;
					tempbaseprice = tempArray[i].base_price;

					if (tempvtid in tempA_S_Hash == false) {
						console.log("Hash doesn't contain tempvtid:"+tempvtid);
						tempA_S_Hash[tempvtid] = []; //{};
						tempASVehiclesHash[tempvtid] = [];
					}

					if (tempstid in tempA_S_Hash[tempvtid] == false) {
						console.log("Hash doesn't contain tempstid:"+tempstid);
						tempA_S_Hash[tempvtid][tempstid] = []; //{};
					}

					serviceypeExists = undefined;
					tempLength = tempASVehiclesHash[tempvtid].length;
					console.log("lenght:"+tempLength);
					for(var j = 0;
						j < tempLength;
						j++ ) {
							if (tempASVehiclesHash[tempvtid][j].service_type_id === tempstid) {
								serviceypeExists = 1;
							}
					}

					if ( typeof serviceypeExists === 'undefined' ) {
						console.log("for adding service type");
						tempASVehiclesHash[tempvtid].
							push({
								'service_type_id' : tempstid
							});

					}

					tempA_S_Hash[tempvtid][tempstid][tempvcid] = {};
					tempA_S_Hash[tempvtid][tempstid][tempvcid]['base_price'] = tempbaseprice;

				};
			}

			console.log("tempASVId_Array:"+tempASVId_Array);
			console.log("tempA_S_Hash:"+
				JSON.stringify(tempA_S_Hash));
			console.log("tempASVehiclesHash:"+
				JSON.stringify(tempASVehiclesHash));

			x.setState({				
					A_S_Hash : tempA_S_Hash,
					ASVehiclesHash : tempASVehiclesHash,
					ASVId_Array : tempASVId_Array
				})
		});

	} // end of - getAvailableServiceData

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
			newState["AvailableServicesImagesHash"] = tempAvailableServiceImagesHash;
			x.setState(newState);						

		});

	} // end of - getImagesData

	componentWillMount(){
		// This method: componentWillMount is being 
		//   called the first time the component is loaded right before
		//   the component is affected to the page 
	
		this.getVehicleTypesData();
		this.getServiceTypesData();
		this.getVehicleConditionData();
		this.getImagesData();
		this.getAvailableServiceData();

	} // end of - componentWillMount(){

  render() {
		return (
			<div className="availableservicesComponent">

    		<h1>Hello, Price page under construction</h1>;

				{this.state.ASVId_Array &&
					this.state.ASVId_Array.map(
						(tempvehicleTypeId, asvidrownum) => (

					   	<div className="col-md-2"><DropdownButton
			    			title={
			    				(
				    				this.state.V_T_Hash &&
				    				this.state.V_T_Hash[tempvehicleTypeId]
			    				) ?
				    				this.state.V_T_Hash[tempvehicleTypeId].display_text :
			    					"Vehicle Types"
			    			}
								name={"VehicleTypesName"+tempvehicleTypeId}
			    			onSelect={this.vehicleSelect}>
			    			{
			    				this.state.V_T_Array &&
			    				this.state.V_T_Array.map(
				    				(vehicles, vehicledropdownindex) => (
					      			<MenuItem eventKey={'rowcol_'+vehicledropdownindex}>
					      				{vehicles.display_text}
					      			</MenuItem>
				      			)
			      			)
			      		}
			    		</DropdownButton></div>

						)
					)
				}

			</div>
		)

  }
}