using System.Collections;
using System.Collections.Generic;
using UnityEngine;



public class Spawner : MonoBehaviour
{
    struct Cube
    {
        public int x;
        public int y;
        public int z;
        public int id;
    }

    struct Coordinate
    {
        public int x;
        public int y;
        public int z;
    }
    
    public GameObject cube;
    List<Cube> coords = new List<Cube>(); // crea lista de cubos
    List<Coordinate> nextCoords = new List<Coordinate>(); //crea lista de coordenadas a donde se tienen que mover los cubos

    public int num = 8; //numero de cubos
    public int x = -50; //coordenadas donde al principio van a aparecer los cubos
    public int y = 5;
    public int z = -50;    

    private IEnumerator coroutine;

    public float speed = 1.0f;

    void Start()
    {
        for (int i = 0; i < num; i++) //inicializa los cubos
        {
            Cube point = new Cube();
            point.x = x;
            point.y = y;
            point.z = z;
            point.id = i+1;
            coords.Add(point);
            x += 10;
            z += 10;
        }
        for (int i = 0; i < num; i++)
        {
            Coordinate coord = new Coordinate(); //inicializa las nuevas coordenadas
            coord.x = x*-1;
            coord.y = y*-1;
            coord.z = z*-1;
            nextCoords.Add(coord);
            x += 10;
            z += 10;
        }

        for (int i = 0; i < num; i++)
        {
            Vector3 position = new Vector3 (coords[i].x, coords[i].y, coords[i].z);
            Instantiate(cube, position, Quaternion.identity); //aparece los cubitos en maicra el quatierion es para que no giren los cubos y aparezcan de pie
        }
        coroutine = WaitAndPrint(5.0f); //se ejecuta cada cinco segundos la coroutine

        print("Starting " + Time.time); 

        StartCoroutine(coroutine);

        print("Before WaitAndPrint Finishes " + Time.time);
    }

    private IEnumerator WaitAndPrint(float waitTime)
    {
        while (true)
        {
            yield return new WaitForSeconds(waitTime);
            GameObject[] obj=GameObject.FindGameObjectsWithTag("TestObject"); // se crea la lista de cubos tienen que estar en el tag de TestObject para que jale 
            for(int i=0;i<obj.Length;i++){
                obj[i].transform.position=new Vector3(nextCoords[i].x,5,nextCoords[i].z); // se mueven a las nuevas coordenadas pero sin el movetowards
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        // Move our position a step closer to the target.
        
        
    }
}

