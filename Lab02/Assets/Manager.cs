using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Manager : MonoBehaviour
{
	public Text DateTime;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
		string time = System.DateTime.UtcNow.ToLocalTime().ToString("dd-MM-yyyy HH:mm:ss");
		DateTime.text = time;
        
    }
	public void BackLogin(){
		SceneManager.LoadScene("LoginScene");
	}
}
