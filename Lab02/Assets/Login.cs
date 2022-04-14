using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Login : MonoBehaviour
{	public Text Message;
	public InputField BrokerURI;
	public InputField Username;
	public InputField Password;
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Hello");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
	public void LoginAction (){
		if (Username.text == "bkiot" && Password.text == "12345678") {
			SceneManager.LoadScene("HomeScene");
		}
		else {
			Message.text = "Username or password is incorrect";
		}
	}
}
