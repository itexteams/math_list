import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang4_p2_b2_c1_hh11(self):
            # Khai báo biến
            a1=randint(2,10)
            a=a1*2
            b1=randint(2,10)
            b=b1*2
            while a==b:
                a1=randint(2,10)
                a=a1*2
                b1=randint(2,10)
                b=b1*2
            s=a1*b1

            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật có $AB=%s, AD=%s$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $SA, SB, SC$ và $SD$. \n'''%(latex(a),latex(b))
            hinhve=('\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=0.8,line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm] \n'
                                '\\clip(-1.4244394472247963,-0.745609730923229) rectangle (5.842639990831729,5.682413568492722);\n'
                                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,2.);\n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (5.,2.);\n'
                                '\\draw (5.,2.)-- (3.,0.);\n'
                                '\\draw (3.,0.)-- (0.,0.);\n'
                                '\\draw (0.,0.)-- (2.,5.);\n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.,5.)-- (2.,2.);\n'
                                '\\draw (2.,5.)-- (3.,0.);\n'
                                '\\draw (2.,5.)-- (5.,2.);\n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.,3.5)-- (3.5,3.5);\n'
                                '\\draw (3.5,3.5)-- (2.5,2.5);\n'
                                '\\draw (2.5,2.5)-- (1.,2.5);\n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.,2.5)-- (2.,3.5);\n'
                                '\\draw (1.803793492968611,5.6) node[anchor=north west] {$S$};\n'
                                '\\draw (-0.3,0) node[anchor=north west] {$B$};\n'
                                '\\draw (1.8,2) node[anchor=north west] {$A$};\n'
                                '\\draw (5,2.3) node[anchor=north west] {$D$};\n'
                                '\\draw (2.77084124597809,0.03656124577561453) node[anchor=north west] {$C$};\n'
                                '\\draw (0.5665412207358954,2.866598052376885) node[anchor=west] {$N$};\n'
                                '\\draw (1.5335889737453743,4.004301291211567) node[anchor=north west] {$M$};\n'
                                '\\draw (3.5814548036478,3.9616374197552657) node[anchor=north west] {$Q$};\n'
                                '\\draw (2.6286283411237545,2.866598052376885) node[anchor=north west] {$P$};\n'
                            '\\end{tikzpicture}\n'
                        '\\end{center}\n')

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $AB$ và $MN$ song song với nhau'
            nb_da_1_s = '$AB$ và $MQ$ song song với nhau'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $AB$ và $PQ$ song song với nhau'
            nb_da_2_s = '$AB$ và $SC$ song song với nhau'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '\\True $MN$ và $CD$ song song với nhau'
            nb_da_3_s = '$MN$ và $AC$ song song với nhau'
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            nb_da_4_d = '\\True $MN$ và $PQ$ song song với nhau'
            nb_da_4_s = '$MN$ và $BD$ song song với nhau'
            list_nb_da_4=[nb_da_4_d,nb_da_4_s]
            nb_da_4=random.choice(list_nb_da_4)

            nb_da_5_d = '\\True $MQ$ và $BC$ song song với nhau'
            nb_da_5_s = '$MQ$ và $CD$ song song với nhau'
            list_nb_da_5=[nb_da_5_d,nb_da_5_s]
            nb_da_5=random.choice(list_nb_da_5)

            nb_da_6_d = '\\True $MQ$ và $NP$ song song với nhau'
            nb_da_6_s = '$NP$ và $CD$ song song với nhau'
            list_nb_da_6=[nb_da_6_d,nb_da_6_s]
            nb_da_6=random.choice(list_nb_da_6)

            nb_da_7_d = '\\True $NP$ và $AD$ song song với nhau'
            nb_da_7_s = '$NP$ và $AB$ song song với nhau'
            list_nb_da_7=[nb_da_7_d,nb_da_7_s]
            nb_da_7=random.choice(list_nb_da_7)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2,nb_da_3,nb_da_4,nb_da_5,nb_da_6,nb_da_7]

            # Nội dung lời giải
            loigiai_nb_1 = ('Vì $MN$ là đường trung bình của $\\triangle SAB$ nên $MN//AB$.\\\\ \n'
                            '$MN$ và $BD$ không cùng nằm trên một mặt phẳng nên chúng chéo nhau.'
                        )
            loigiai_nb_2 = ('Vì $PQ$ là đường trung bình của $\\triangle SCD$ nên $PQ//CD$.\\\\ \n'
                            'Mà $CD//AB$ (vì $ABCD$ là hình chữ nhật) nên suy ra $AB//PQ$.\\\\ \n'
                            '$AD$ và $SC$ không cùng nằm trên một mặt phẳng nên chúng chéo nhau.'
                        )
            loigiai_nb_3 = ('Vì $MN$ là đường trung bình của $\\triangle SAB$ nên $MN//AB$.\\\\ \n'
                            'Mà $AB//CD$ (vì $ABCD$ là hình chữ nhật) nên suy ra $MN//CD$.\\\\ \n'
                            '$MN$ và $AC$ không cùng nằm trên một mặt phẳng nên chúng chéo nhau.'
                        )
            loigiai_nb_4 = ('Vì $MN$ là đường trung bình của $\\triangle SAB$ nên $MN//AB$.\\\\ \n'
                            'Tương tự $PQ$ là đường trung bình của $\\triangle SCD$ nên $PQ//CD$.\\\\ \n'
                            'Mà $AB//CD$ (vì $ABCD$ là hình chữ nhật) nên suy ra $MN//PQ$.\\\\ \n'
                            '$MN$ và $BD$ không cùng nằm trên một mặt phẳng nên chúng chéo nhau.'
                        )
            loigiai_nb_5 = ('Vì $MQ$ là đường trung bình của $\\triangle SAD$ nên $MQ//AD$.\\\\ \n'
                            'Mà $AD//BC$ (vì $ABCD$ là hình chữ nhật) nên suy ra $MQ//BC$.\\\\ \n'
                            '$MQ$ và $CD$ không cùng nằm trên một mặt phẳng nên chúng chéo nhau.'
                        )
            loigiai_nb_6 = ('Vì $MQ$ là đường trung bình của $\\triangle SAD$ nên $MQ//AD$.\\\\ \n'
                            'Tương tự $NP$ là đường trung bình của $\\triangle SBC$ nên $NP//BC$.\\\\ \n'
                            'Mà $AD//BC$ (vì $ABCD$ là hình chữ nhật) nên suy ra $MQ//NP$.\\\\ \n'
                            '$NP$ và $CD$ không cùng nằm trên một mặt phẳng nên chúng chéo nhau.'
                        )
            loigiai_nb_7 = ('Vì $NP$ là đường trung bình của $\\triangle SBC$ nên $NP//BC$.\\\\ \n'
                            'Mà $AD//BC$ (vì $ABCD$ là hình chữ nhật) nên suy ra $NP//AD$.\\\\ \n'
                            '$NP$ và $AD$ không cùng nằm trên một mặt phẳng nên chúng chéo nhau.'
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3,loigiai_nb_4,loigiai_nb_5,loigiai_nb_6,loigiai_nb_7]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $MN=\\dfrac{1}{2} CD$'
            th_da_1_s = '$MN=\\dfrac{1}{3} CD$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $PQ=\\dfrac{1}{2} AB$'
            th_da_2_s = '$PQ=\\dfrac{1}{4} AB$'
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True $MQ=\\dfrac{1}{2} BC$'
            th_da_3_s = '$MQ=\\dfrac{1}{3} BC$'
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)

            th_da_4_d = '\\True $NP=\\dfrac{1}{2} AD$'
            th_da_4_s = '$NP=\\dfrac{1}{4} AD$'
            list_th_da_4=[th_da_4_d,th_da_4_s]
            th_da_4=random.choice(list_th_da_4)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2,th_da_3,th_da_4]

            # Nội dung lời giải
            loigiai_th_1 = ('Vì $MN$ là đường trung bình của  $\\triangle SAB$ nên $MN=\\dfrac{1}{2} AB$.\\\\ \n'
                            'Mà $AB=CD$ (vì $ABCD$ là hình chữ nhật) nên suy ra $MN=\\dfrac{1}{2} CD$. '
                        )
            loigiai_th_2 = ('Vì $PQ$ là đường trung bình của  $\\triangle SCD$ nên $PQ=\\dfrac{1}{2} CD$.\\\\ \n'
                            'Mà $CD=AB$ (vì $ABCD$ là hình chữ nhật) nên suy ra $PQ=\\dfrac{1}{2} AB$. '
                        )
            loigiai_th_3 = ('Vì $MQ$ là đường trung bình của  $\\triangle SAD$ nên $MQ=\\dfrac{1}{2} AD$.\\\\ \n'
                            'Mà $AD=BC$ (vì $ABCD$ là hình chữ nhật) nên suy ra $MQ=\\dfrac{1}{2} BC$. '
                        )
            loigiai_th_4 = ('Vì $NP$ là đường trung bình của  $\\triangle SBC$ nên $NP=\\dfrac{1}{2} BC$.\\\\ \n'
                            'Mà $AD=BC$ (vì $ABCD$ là hình chữ nhật) nên suy ra $NP=\\dfrac{1}{2} AD$. '
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2,loigiai_th_3,loigiai_th_4]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Tứ giác $MNPQ$ là hình chữ nhật'
            vd_da_1_s = 'Tứ giác $MNPQ$ là hình thoi'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Vì $MN$ là đường trung bình của $\\triangle SAB$ nên $\\heva{&MN//AB\\\\& MN=\\dfrac{1}{2}AB=%s}$ (1).\\\\ \n'
                            'Tương tự $PQ$ là đường trung bình của $\\triangle SCD$ nên $\\heva{&PQ//AB\\\\& PQ=\\dfrac{1}{2}CD=%s}$ (2).\\\\ \n'
                            'Mặt khác tứ giác $ABCD$ là hình chữ nhật nên ta có $\\heva{&AB//CD\\\\&AB=CD}$ (3).\\\\ \n'
                            'Từ (1), (2), (3) ta có $\\heva{&MN//PQ//AB//CD\\\\& MN=PQ=\\dfrac{1}{2} AB=\\dfrac{1}{2} CD=%s}$.\\\\ \n'
                            'Suy ra tứ giác $MNPQ$ là hình bình hành (vì có một cặp cạnh đối $MN, PQ$ song song và bằng nhau).\\\\ \n'
                            'Vì $MP$ là đường trung bình của $\\triangle SAC$ nên $MP=\\dfrac{1}{2}AC$.\\\\ \n' 
                            'Vì $NQ$ là đường trung bình của $\\triangle SBD$ nên $NQ=\\dfrac{1}{2}BD$.\\\\ \n' 
                            'Mà $AC=BD$ nên suy ra $MP=NQ$.\\\\ \n'
                            'Do đó tứ giác $MNPQ$ là hình chữ nhật vì có tứ giác $MNPQ$ là hình bình hành có hai đường chéo bằng nhau.'
                            %(latex(a1),latex(a1),latex(a1))
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Diện tích tứ giác $MNPQ$ bằng $%s$'%(latex(s))
            vdc_da_1_s = ' Diện tích tứ giác $MNPQ$ bằng $%s$'%(latex(s*2))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Vì $MQ$ là đường trung bình của $\\triangle SAD$ nên $MQ=\\dfrac{1}{2}AD=%s$.\\\\ \n'
                            'Vì tứ giác $MNPQ$ là hình chữ nhật nên diện tích của tứ giác $MNPQ$ là\\\\ \n'
                            '\\hspace*{1cm} $S_{MNPQ}=MQ\\cdot MP=%s\\cdot%s=%s$.'%(latex(b1),latex(a1),latex(b1),latex(s))
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'+hinhve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

