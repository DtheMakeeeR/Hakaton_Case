using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web;
using System.Windows.Forms;

namespace UI
{
    public partial class Form1 : Form
    {
        ProcessStartInfo processStartInfo = new ProcessStartInfo("../../../Src/Python/python.exe");
        void FieldsClear()
        {
            processStartInfo.Arguments = "../../../Src/TableCreator.py ";
            formFileName1.Clear();
            formFileName2.Clear();
            formComboBox1.SelectedIndex = -1;
            formComboBox1.Items.Clear();
        }
        public Form1()
        {
            InitializeComponent();
            processStartInfo.Arguments = "../../../Src/TableCreator.py ";
            processStartInfo.UseShellExecute = false;
            processStartInfo.RedirectStandardError = true;
            processStartInfo.RedirectStandardOutput = true;
            formComboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }


        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog opd = new OpenFileDialog();
            string path = null;
            if (opd.ShowDialog() == DialogResult.OK)
            {
                path = opd.FileName;
                formFileName1.Text = path;
            }                                
        }

        private void button2_Click(object sender, EventArgs e)
        {
            OpenFileDialog opd = new OpenFileDialog();
            string path = null;
            if (opd.ShowDialog() == DialogResult.OK)
            {
                path = opd.FileName;
                formFileName2.Text = path;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            OpenFileDialog opd = new OpenFileDialog();
            opd.Multiselect = true;
            string[] pathes = null;
            if (opd.ShowDialog() == DialogResult.OK)
            {
                pathes = opd.FileNames;
                foreach (var path in pathes)
                {
                    formComboBox1.Items.Add(path);                    
                }
                formComboBox1.SelectedIndex = 0;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            FieldsClear();            
        }

        private void button5_Click(object sender, EventArgs e)
        {
            processStartInfo.Arguments += "\"" + formFileName1.Text + "\"" + " ";
            processStartInfo.Arguments += "\"" + formFileName2.Text + "\"" + " ";
            foreach (var path in formComboBox1.Items)
            {
                processStartInfo.Arguments += "\"" + path + "\"" + " ";
            }
            string errors = "";
            using (var process = Process.Start(processStartInfo))
            {
                errors = process.StandardError.ReadToEnd();
            }
            if (errors != "")
            {
                FieldsClear();
                MessageBox.Show(errors, "Error");
                return;
            }
            ProcessStartInfo modelProcess = new ProcessStartInfo("../../../Src/Python/python.exe");
            modelProcess.Arguments = "../../../Src/AI_script.py";
            modelProcess.RedirectStandardError = true;
            modelProcess.RedirectStandardOutput = true;
            modelProcess.UseShellExecute = false;
            using (var process = Process.Start(modelProcess))
            {
                errors = process.StandardError.ReadToEnd();
            }
            if (errors != "")
            {
                FieldsClear();
                MessageBox.Show(errors, "Error");
                return;
            }
            FieldsClear();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            formFileName1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            formFileName2.Clear();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            formComboBox1.SelectedIndex = -1;
            formComboBox1.Items.Clear();
        }
    }
}
