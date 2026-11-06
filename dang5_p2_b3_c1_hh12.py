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


def bt_dang5_p2_b3_c1_hh12(self):
            # Khai báo biến
            xa=randint(-9,9)
            ya=randint(-9,9)
            za=randint(-9,9)
            xb=randint(-9,9)
            yb=randint(-9,9)
            zb=randint(-9,9)
            k=randint(2,5)
            xm=nsimplify((xa+k*xb)/(1+k))
            ym=nsimplify((ya+k*yb)/(1+k))
            zm=nsimplify((za+k*zb)/(1+k))
            while xa==0 or ya==0 or za==0 or xb==0 or yb==0 or zb==0 or xa==xb:
                xa=randint(-9,9)
                ya=randint(-9,9)
                za=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)
                zb=randint(-9,9)
                xm=nsimplify((xa+k*xb)/(1+k))
                ym=nsimplify((ya+k*yb)/(1+k))
                zm=nsimplify((za+k*zb)/(1+k))


            # Nội dung câu hỏi
            noidungcauhoi = ('Trong không gian $Oxyz$, cho hai điểm $A(%s;%s;%s), B(%s;%s;%s)$.'
                            %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Vectơ đơn vị của trục $Ox$ là $\\vec{i}=(1;0;0)$'
            nb_da_1_s = 'Vectơ đơn vị của trục $Ox$ là $\\vec{i}=(0;1;0)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Vectơ đơn vị của trục $Oy$ là $\\vec{j}=(0;1;0)$'
            nb_da_2_s = 'Vectơ đơn vị của trục $Oy$ là $\\vec{j}=(0;0;1)$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '\\True Vectơ đơn vị của trục $Oz$ là $\\vec{k}=(0;0;1)$'
            nb_da_3_s = 'Vectơ đơn vị của trục $Oy$ là $\\vec{j}=(1;0;0)$'
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2, nb_da_3]

            # Nội dung lời giải
            loigiai_nb_1 = ('Vectơ đơn vị của trục $Ox$ là $\\vec{i}=(1;0;0)$.'
                        )
            loigiai_nb_2 = ('Vectơ đơn vị của trục $Oy$ là $\\vec{j}=(0;1;0)$.'
                        )
            loigiai_nb_3 = ('Vectơ đơn vị của trục $Oz$ là $\\vec{k}=(0;0;1)$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\vec{AB}=(%s;%s;%s)$'%(latex(xb-xa),latex(yb-ya),latex(zb-za))
            th_da_1_s = ' $\\vec{AB}=(%s;%s;%s)$'%(latex(-xb+xa),latex(-yb+ya),latex(-zb+za))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\vec{BA}=(%s;%s;%s)$'%(latex(-xb+xa),latex(-yb+ya),latex(-zb+za))
            th_da_2_s = '$\\vec{BA}=(%s;%s;%s)$'%(latex(xb-xa),latex(yb-ya),latex(zb-za))
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('$\\vec{AB}=(%s;%s;%s)$.'%(latex(xb-xa),latex(yb-ya),latex(zb-za))
                        )
            loigiai_th_2 = ('$\\vec{BA}=(%s;%s;%s)$.'%(latex(-xb+xa),latex(-yb+ya),latex(-zb+za))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Hình chiếu của điểm $A$ lên mặt phẳng $(Oxy)$ có tọa độ là $(%s;%s;0)$'%(latex(xa),latex(ya))
            vd_da_1_s = 'Hình chiếu của điểm $A$ lên mặt phẳng $(Oxy)$ có tọa độ là $(-%s;-%s;0)$'%(latex(xa),latex(ya))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Hình chiếu của điểm $A$ lên mặt phẳng $(Oxz)$ có tọa độ là $(%s;0;%s)$'%(latex(xa),latex(za))
            vd_da_2_s = 'Hình chiếu của điểm $A$ lên mặt phẳng $(Oxz)$ có tọa độ là $(%s;%s;0)$'%(latex(xa),latex(ya))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True Hình chiếu của điểm $A$ lên mặt phẳng $(Oyz)$ có tọa độ là $(0;%s;%s)$'%(latex(ya),latex(za))
            vd_da_3_s = 'Hình chiếu của điểm $A$ lên mặt phẳng $(Oyz)$ có tọa độ là $(%s;0;0)$'%(latex(xa))
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)

            vd_da_4_d = '\\True Hình chiếu của điểm $B$ lên mặt phẳng $(Oxy)$ có tọa độ là $(%s;%s;0)$'%(latex(xb),latex(yb))
            vd_da_4_s = 'Hình chiếu của điểm $B$ lên mặt phẳng $(Oxy)$ có tọa độ là $(-%s;-%s;0)$'%(latex(xb),latex(yb))
            list_vd_da_4=[vd_da_4_d,vd_da_4_s]
            vd_da_4=random.choice(list_vd_da_4)

            vd_da_5_d = '\\True Hình chiếu của điểm $B$ lên mặt phẳng $(Oxz)$ có tọa độ là $(%s;0;%s)$'%(latex(xb),latex(zb))
            vd_da_5_s = 'Hình chiếu của điểm $B$ lên mặt phẳng $(Oxz)$ có tọa độ là $(%s;%s;0)$'%(latex(xb),latex(yb))
            list_vd_da_5=[vd_da_5_d,vd_da_5_s]
            vd_da_5=random.choice(list_vd_da_5)

            vd_da_6_d = '\\True Hình chiếu của điểm $B$ lên mặt phẳng $(Oyz)$ có tọa độ là $(0;%s;%s)$'%(latex(yb),latex(zb))
            vd_da_6_s = 'Hình chiếu của điểm $B$ lên mặt phẳng $(Oyz)$ có tọa độ là $(%s;0;0)$'%(latex(xb))
            list_vd_da_6=[vd_da_6_d,vd_da_6_s]
            vd_da_6=random.choice(list_vd_da_6)

            vd_da_7_d = '\\True Hình chiếu của điểm $A$ lên trục $Ox$ có tọa độ là $(%s;0;0)$'%(latex(xa))
            vd_da_7_s = 'Hình chiếu của điểm $A$ lên mặt phẳng $Ox$ có tọa độ là $(0;%s;%s)$'%(latex(ya),latex(za))
            list_vd_da_7=[vd_da_7_d,vd_da_7_s]
            vd_da_7=random.choice(list_vd_da_7)

            vd_da_8_d = '\\True Hình chiếu của điểm $A$ lên trục $Oy$ có tọa độ là $(0;%s;0)$'%(latex(ya))
            vd_da_8_s = 'Hình chiếu của điểm $A$ lên mặt phẳng $Oy$ có tọa độ là $(0;%s;%s)$'%(latex(ya),latex(za))
            list_vd_da_8=[vd_da_8_d,vd_da_8_s]
            vd_da_8=random.choice(list_vd_da_8)

            vd_da_9_d = '\\True Hình chiếu của điểm $A$ lên trục $Oz$ có tọa độ là $(0;0;%s)$'%(latex(za))
            vd_da_9_s = 'Hình chiếu của điểm $A$ lên mặt phẳng $Oz$ có tọa độ là $(%s;%s;0)$'%(latex(xa),latex(ya))
            list_vd_da_9=[vd_da_9_d,vd_da_9_s]
            vd_da_9=random.choice(list_vd_da_9)

            vd_da_10_d = '\\True Hình chiếu của điểm $B$ lên trục $Ox$ có tọa độ là $(%s;0;0)$'%(latex(xb))
            vd_da_10_s = 'Hình chiếu của điểm $B$ lên mặt phẳng $Ox$ có tọa độ là $(0;%s;%s)$'%(latex(yb),latex(zb))
            list_vd_da_10=[vd_da_10_d,vd_da_10_s]
            vd_da_10=random.choice(list_vd_da_10)

            vd_da_11_d = '\\True Hình chiếu của điểm $B$ lên trục $Oy$ có tọa độ là $(0;%s;0)$'%(latex(yb))
            vd_da_11_s = 'Hình chiếu của điểm $B$ lên mặt phẳng $Oy$ có tọa độ là $(0;%s;%s)$'%(latex(yb),latex(zb))
            list_vd_da_11=[vd_da_11_d,vd_da_11_s]
            vd_da_11=random.choice(list_vd_da_11)

            vd_da_12_d = '\\True Hình chiếu của điểm $B$ lên trục $Oz$ có tọa độ là $(0;0;%s)$'%(latex(zb))
            vd_da_12_s = 'Hình chiếu của điểm $B$ lên mặt phẳng $Oz$ có tọa độ là $(%s;%s;0)$'%(latex(xb),latex(yb))
            list_vd_da_12=[vd_da_12_d,vd_da_12_s]
            vd_da_12=random.choice(list_vd_da_12)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2,vd_da_3,vd_da_4,vd_da_5,vd_da_6,vd_da_7,vd_da_8,vd_da_9,vd_da_10,vd_da_11,vd_da_12]

            # Nội dung lời giải
            loigiai_vd_1 = ('Hình chiếu của điểm $A$ lên mặt phẳng $(Oxy)$ có tọa độ là $(%s;%s;0)$.'%(latex(xa),latex(ya))
                        )
            loigiai_vd_2 = ('Hình chiếu của điểm $A$ lên mặt phẳng $(Oxz)$ có tọa độ là $(%s;0;%s)$.'%(latex(xa),latex(za))
                        )
            loigiai_vd_3 = ('Hình chiếu của điểm $A$ lên mặt phẳng $(Oyz)$ có tọa độ là $(0;%s;%s)$.'%(latex(ya),latex(za))
                        )
            loigiai_vd_4 = ('Hình chiếu của điểm $B$ lên mặt phẳng $(Oxy)$ có tọa độ là $(%s;%s;0)$.'%(latex(xb),latex(yb))
                        )
            loigiai_vd_5 = ('Hình chiếu của điểm $B$ lên mặt phẳng $(Oxz)$ có tọa độ là $(%s;0;%s)$.'%(latex(xb),latex(zb))
                        )
            loigiai_vd_6 = ('Hình chiếu của điểm $B$ lên mặt phẳng $(Oyz)$ có tọa độ là $(0;%s;%s)$.'%(latex(yb),latex(zb))
                        )
            loigiai_vd_7 = ('Hình chiếu của điểm $A$ lên trục $Ox$ có tọa độ là $(%s;0;0)$.'%(latex(xa))
                        )
            loigiai_vd_8 = ('Hình chiếu của điểm $A$ lên trục $Oy$ có tọa độ là $(0;%s;0)$.'%(latex(ya))
                        )
            loigiai_vd_9 = ('Hình chiếu của điểm $A$ lên trục $Oz$ có tọa độ là $(0;0;%s)$.'%(latex(za))
                        )
            loigiai_vd_10 = ('Hình chiếu của điểm $B$ lên trục $Ox$ có tọa độ là $(%s;0;0)$.'%(latex(xb))
                        )
            loigiai_vd_11 = ('Hình chiếu của điểm $B$ lên trục $Oy$ có tọa độ là $(0;%s;0)$.'%(latex(yb))
                        )
            loigiai_vd_12 = ('Hình chiếu của điểm $B$ lên trục $Oz$ có tọa độ là $(0;0;%s)$.'%(latex(zb))
                        )



            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2,loigiai_vd_3,loigiai_vd_4,loigiai_vd_5,loigiai_vd_6,loigiai_vd_7,loigiai_vd_8,loigiai_vd_9,loigiai_vd_10,loigiai_vd_11,loigiai_vd_12]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Gọi $M$ là điểm nằm trên đoạn $AB$ sao cho $MA=%sMB$. Toạ độ của điểm $M$ là $\\left(%s;%s;%s\\right)$'%(latex(k),latex(xm),latex(ym),latex(zm))
            vdc_da_1_s = 'Gọi $M$ là điểm nằm trên đoạn $AB$ sao cho $MA=%sMB$. Toạ độ của điểm $M$ là $\\left(%s;%s;%s\\right)$'%(latex(k),latex(xm),latex(-ym),latex(zm+1))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Vì $M$ thuộc đoạn $AB$ nên hai vectơ $\\vec{MA}$ và $\\vec{MB}$ ngược hướng.\\\\ \n'
                            'Mà $MA=%sMB$ nên suy ra $\\vec{MA}=-%s\\vec{MB}$.\\\\ \n'
                            'Gọi $M(x;y;z)$ ta có\\\\ \n'
                            '\\hspace*{1cm}$\\vec{MA}=-%s\\vec{MB}\\Leftrightarrow \\vec{MA}+%s\\vec{MB}=\\vec{0}\\Leftrightarrow\\heva{&x=\\dfrac{%s+%s\\cdot (%s)}{1+%s}\\\\&y=\\dfrac{%s+%s\\cdot (%s)}{1+%s}\\\\&z=\\dfrac{%s+%s\\cdot (%s)}{1+%s}}\\Leftrightarrow\\heva{&x=%s\\\\&y=%s\\\\&z=%s}.$\\\\ \n'
                            'Vậy tọa độ của điểm $M$ là $\\left(%s;%s;%s\\right)$.'
                            %(latex(k),latex(k),latex(k),latex(k),
                            latex(xa),latex(k),latex(xb),latex(k),
                            latex(ya),latex(k),latex(yb),latex(k),
                            latex(za),latex(k),latex(zb),latex(k),
                            latex(xm),latex(ym),latex(zm),
                            latex(xm),latex(ym),latex(zm)


                            )
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
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-')
            return content

