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


def bt_dang3_p2_b3_c1_hh12(self):
            # Khai báo biến
            x1=randint(-8,8)
            y1=randint(-8,8)
            z1=randint(-8,8)
            x2=randint(-8,8)
            y2=randint(-8,8)
            z2=randint(-8,8)
            x3=randint(-8,8)
            y3=randint(-8,8)
            z3=randint(-8,8)
            dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
            dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2+(z3-z1)**2))
            dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2+(z3-z2)**2))
            hd=(y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
            td=(z2-z1)*(x3-x1)-(x2-x1)*(z3-z1)
            cd=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
            k=randint(-5,5)

            while hd==0 or td==0 or cd==0 or k==0:
                x1=randint(-8,8)
                y1=randint(-8,8)
                z1=randint(-8,8)
                x2=randint(-8,8)
                y2=randint(-8,8)
                z2=randint(-8,8)
                x3=randint(-8,8)
                y3=randint(-8,8)
                z3=randint(-8,8)
                hd=(y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
                td=(z2-z1)*(x3-x1)-(x2-x1)*(z3-z1)
                cd=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
                k=randint(-5,5)
            xn=nsimplify((x1+x2)/2)
            yn=nsimplify((y1+y2)/2)
            zn=nsimplify((z1+z2)/2)
            xp=nsimplify((x1+x3)/2)
            yp=nsimplify((y1+y3)/2)
            zp=nsimplify((z1+z3)/2)
            xm=nsimplify((x2+x3)/2)
            ym=nsimplify((y2+y3)/2)
            zm=nsimplify((z2+z3)/2)
            dam=nsimplify(sqrt((xm-x1)**2+(ym-y1)**2+(zm-z1)**2))
            dcn=nsimplify(sqrt((xn-x3)**2+(yn-y3)**2+(zn-z3)**2))
            dbp=nsimplify(sqrt((xp-x2)**2+(yp-y2)**2+(zp-z2)**2))
            dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
            dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2+(z3-z1)**2))
            dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2+(z3-z2)**2))
            cv=dab+dac+dbc
            ta=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)+(z2-z1)*(z3-z1)
            tb=(x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)+(z1-z2)*(z3-z1)
            tc=(x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)+(z1-z3)*(z2-z3)
            cosa=nsimplify(ta/(dab*dac))
            cosb=nsimplify(tb/(dab*dbc))
            cosc=nsimplify(tc/(dbc*dac))
            xd=x3-x2+x1
            yd=y3-y2+y1
            zd=z3-z2+z1
            t_1=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)+(z2-z1)*(z3-z1)
            t_2=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)+(z2-z1)*(z3-z2)
            t_3=(x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)+(z3-z1)*(z3-z2)
            xi=nsimplify((x1-x2)/k+x3)
            yi=nsimplify((y1-y2)/k+y3)
            zi=nsimplify((z1-z2)/k+z3)
            # Nội dung câu hỏi
            noidungcauhoi = '''Trong không gian $Oxyz$, cho tam giác giác $ABC$ với $A(%s;%s;%s), B(%s;%s;%s)$ và $C(%s;%s;%s)$. \n'''%(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),latex(x3),latex(y3),latex(z3))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Toạ độ vectơ $\\vec{AB}=(%s;%s;%s)$'%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
            nb_da_1_s = 'Toạ độ vectơ $\\vec{AB}=(%s;%s;%s)$'%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Toạ độ vectơ $\\vec{AC}=(%s;%s;%s)$'%(latex(x3-x1),latex(y3-y1),latex(z3-z1))
            nb_da_2_s = 'Toạ độ vectơ $\\vec{AC}=(%s;%s;%s)$'%(latex(-x3+x1),latex(-y3+y1),latex(-z3+z1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '\\True Toạ độ vectơ $\\vec{BC}=(%s;%s;%s)$'%(latex(x3-x2),latex(y3-y2),latex(z3-z2))
            nb_da_3_s = 'Toạ độ vectơ $\\vec{BC}=(%s;%s;%s)$'%(latex(-x3+x2),latex(-y3+y2),latex(-z3+z2))
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            nb_da_4_d = '\\True Toạ độ trọng tâm $G$ của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((x1+x2+x3)/3)),latex(nsimplify((y1+y2+y3)/3)),latex(nsimplify((z1+z2+z3)/3)))
            nb_da_4_s = 'Toạ độ trọng tâm $G$ của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((x1+x2+x3)/3)),latex(nsimplify((y1+y2+y3)/3)),latex(nsimplify((-z1-z2-z3)/3)))
            list_nb_da_4=[nb_da_4_d,nb_da_4_s]
            nb_da_4=random.choice(list_nb_da_4)

            nb_da_5_d = '\\True Toạ độ trung điểm $N$ của cạnh $AB$ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((x1+x2)/2)),latex(nsimplify((y1+y2)/2)),latex(nsimplify((z1+z2)/2)))
            nb_da_5_s = 'Toạ độ trung điểm $N$ của cạnh $AB$ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((-x1-x2)/2)),latex(nsimplify((-y1-y2)/2)),latex(nsimplify((-z1-z2)/2)))
            list_nb_da_5=[nb_da_5_d,nb_da_5_s]
            nb_da_5=random.choice(list_nb_da_5)

            nb_da_6_d = '\\True Toạ độ trung điểm $P$ của cạnh $AC$ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((x1+x3)/2)),latex(nsimplify((y1+y3)/2)),latex(nsimplify((z1+z3)/2)))
            nb_da_6_s = 'Toạ độ trung điểm $P$ của cạnh $AC$ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((-x1-x3)/2)),latex(nsimplify((-y1-y3)/2)),latex(nsimplify((-z1-z3)/2)))
            list_nb_da_6=[nb_da_6_d,nb_da_6_s]
            nb_da_6=random.choice(list_nb_da_6)

            nb_da_7_d = '\\True Toạ độ trung điểm $M$ của cạnh $BC$ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((x2+x3)/2)),latex(nsimplify((y2+y3)/2)),latex(nsimplify((z2+z3)/2)))
            nb_da_7_s = 'Toạ độ trung điểm $M$ của cạnh $BC$ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((-x2-x3)/2)),latex(nsimplify((-y2-y3)/2)),latex(nsimplify((-z2-z3)/2)))
            list_nb_da_7=[nb_da_7_d,nb_da_7_s]
            nb_da_7=random.choice(list_nb_da_7)

            nb_da_8_d = '\\True Toạ độ vectơ $\\vec{BA}=(%s;%s;%s)$'%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
            nb_da_8_s = 'Toạ độ vectơ $\\vec{BA}=(%s;%s;%s)$'%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
            list_nb_da_8=[nb_da_8_d,nb_da_8_s]
            nb_da_8=random.choice(list_nb_da_8)

            nb_da_9_d = '\\True Toạ độ vectơ $\\vec{CA}=(%s;%s;%s)$'%(latex(-x3+x1),latex(-y3+y1),latex(-z3+z1))
            nb_da_9_s = 'Toạ độ vectơ $\\vec{CA}=(%s;%s;%s)$'%(latex(x3-x1),latex(y3-y1),latex(z3-z1))
            list_nb_da_9=[nb_da_9_d,nb_da_9_s]
            nb_da_9=random.choice(list_nb_da_9)

            nb_da_10_d = '\\True Toạ độ vectơ $\\vec{CB}=(%s;%s;%s)$'%(latex(-x3+x2),latex(-y3+y2),latex(-z3+z2))
            nb_da_10_s = 'Toạ độ vectơ $\\vec{CB}=(%s;%s;%s)$'%(latex(x3-x2),latex(y3-y2),latex(z3-z2))
            list_nb_da_10=[nb_da_10_d,nb_da_10_s]
            nb_da_10=random.choice(list_nb_da_10)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2, nb_da_3, nb_da_4, nb_da_5, nb_da_6, nb_da_7, nb_da_8, nb_da_9, nb_da_10]

            # Nội dung lời giải
            loigiai_nb_1 = ('Toạ độ vectơ $\\vec{AB}=(%s;%s;%s)$.'%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
                        )
            loigiai_nb_2 = ('Toạ độ vectơ $\\vec{AC}=(%s;%s;%s)$.'%(latex(x3-x1),latex(y3-y1),latex(z3-z1))
                        )
            loigiai_nb_3 = ('Toạ độ vectơ $\\vec{BC}=(%s;%s;%s)$.'%(latex(x3-x2),latex(y3-y2),latex(z3-z2))
                        )
            loigiai_nb_4 = ('Vì $G$ là trọng tâm của tam giác $ABC$ nên tọa độ của điểm $G$ là $\\left(\\dfrac{%s+%s+%s}{3};\\dfrac{%s+%s+%s}{3};\\dfrac{%s+%s+%s}{3}\\right)$, suy ra $G\\left(%s;%s;%s\\right)$.'%(latex(x1),latex(x2),latex(x3),latex(y1),latex(y2),latex(y3),latex(z1),latex(z2),latex(z3),latex(nsimplify((x1+x2+x3)/3)),latex(nsimplify((y1+y2+y3)/3)),latex(nsimplify((z1+z2+z3)/3)))
                        )
            loigiai_nb_5 = ('Vì $N$ là trung điểm của cạnh $AB$ nên tọa độ của điểm $M$ là $\\left(\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2}\\right)$, suy ra $N\\left(%s;%s;%s\\right)$.'%(latex(x1),latex(x2),latex(y1),latex(y2),latex(z1),latex(z2),latex(nsimplify((x1+x2)/2)),latex(nsimplify((y1+y2)/2)),latex(nsimplify((z1+z2)/2)))
                        )
            loigiai_nb_6 = ('Vì $P$ là trung điểm của cạnh $AC$ nên tọa độ của điểm $N$ là $\\left(\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2}\\right)$, suy ra $P\\left(%s;%s;%s\\right)$.'%(latex(x1),latex(x3),latex(y1),latex(y3),latex(z1),latex(z3),latex(nsimplify((x1+x3)/2)),latex(nsimplify((y1+y3)/2)),latex(nsimplify((z1+z3)/2)))
                        )
            loigiai_nb_7 = ('Vì $M$ là trung điểm của cạnh $BC$ nên tọa độ của điểm $P$ là $\\left(\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2}\\right)$, suy ra $M\\left(%s;%s;%s\\right)$.'%(latex(x2),latex(x3),latex(y2),latex(y3),latex(z2),latex(z3),latex(nsimplify((x2+x3)/2)),latex(nsimplify((y2+y3)/2)),latex(nsimplify((z2+z3)/2)))
                        )
            loigiai_nb_8 = ('Toạ độ vectơ $\\vec{BA}=(%s;%s;%s)$.'%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
                        )
            loigiai_nb_9 = ('Toạ độ vectơ $\\vec{CA}=(%s;%s;%s)$.'%(latex(-x3+x1),latex(-y3+y1),latex(-z3+z1))
                        )
            loigiai_nb_10 = ('Toạ độ vectơ $\\vec{CB}=(%s;%s;%s)$.'%(latex(-x3+x2),latex(-y3+y2),latex(-z3+z2))
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3,loigiai_nb_4,loigiai_nb_5,loigiai_nb_6,loigiai_nb_7,loigiai_nb_8,loigiai_nb_9,loigiai_nb_10]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\vec{AB}\\cdot\\vec{AC}=%s$'%(latex(t_1))
            th_da_1_s = ' $\\vec{AB}\\cdot\\vec{AC}=%s$'%(latex(-t_1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\vec{AB}\\cdot\\vec{BC}=%s$'%(latex(t_2))
            th_da_2_s = '$\\vec{AB}\\cdot\\vec{BC}=%s$'%(latex(-t_2))
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True $\\vec{AC}\\cdot\\vec{BC}=%s$'%(latex(t_3))
            th_da_3_s = '$\\vec{AC}\\cdot\\vec{BC}=%s$'%(latex(-t_3))
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2,th_da_3]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có $\\vec{AB}=(%s;%s;%s)$ và $\\vec{AC}=(%s;%s;%s)$.\\\\ \n'
                            'Suy ra $\\vec{AB}\\cdot\\vec{AC}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'
                            %(latex(x2-x1),latex(y2-y1),latex(z2-z1),latex(x3-x1),latex(y3-y1),latex(z3-z1),latex(x2-x1),latex(x3-x1),latex(y2-y1),latex(y3-y1),latex(z2-z1),latex(z3-z1),latex(t_1))
                            )
            loigiai_th_2 = ('Ta có $\\vec{AB}=(%s;%s;%s)$ và $\\vec{BC}=(%s;%s;%s)$.\\\\ \n'
                            'Suy ra $\\vec{AB}\\cdot\\vec{BC}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'
                            %(latex(x2-x1),latex(y2-y1),latex(z2-z1),latex(x3-x2),latex(y3-y2),latex(z3-z2),latex(x2-x1),latex(x3-x2),latex(y2-y1),latex(y3-y2),latex(z2-z1),latex(z3-z2),latex(t_2))
                            )
            loigiai_th_3 = ('Ta có $\\vec{AC}=(%s;%s;%s)$ và $\\vec{BC}=(%s;%s;%s)$.\\\\ \n'
                            'Suy ra $\\vec{AC}\\cdot\\vec{BC}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'
                            %(latex(x3-x1),latex(y3-y1),latex(z3-z1),latex(x3-x2),latex(y3-y2),latex(z3-z2),latex(x3-x1),latex(x3-x2),latex(y3-y1),latex(y3-y2),latex(z3-z1),latex(z3-z2),latex(t_3))
                            )


            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2, loigiai_th_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án


            vd_da_1_d = '\\True $\\cos \\widehat{BAC}=%s$'%(latex(cosa))
            vd_da_1_s  = '$\\cos \\widehat{BAC}=%s$'%(latex(-cosc))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $\\cos \\widehat{ABC}=%s$'%(latex(cosb))
            vd_da_2_s  = '$\\cos \\widehat{ABC}=%s$'%(latex(-cosa))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True $\\cos \\widehat{ACB}=%s$'%(latex(cosc))
            vd_da_3_s  = '$\\cos \\widehat{ACB}=%s$'%(latex(-cosb))
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)

            vd_da_4_d = '\\True Chu vi của tam giác $ABC$ là $%s$'%(latex(cv))
            vd_da_4_s  = ' Chu vi của tam giác $ABC$ là $%s$'%(latex(2*cv))
            list_vd_da_4=[vd_da_4_d,vd_da_4_s]
            vd_da_4=random.choice(list_vd_da_4)

            vd_da_5_d = '\\True Độ dài đường trung tuyến $AM$ của tam giác $ABC$ là $%s$'%(latex(dam))
            vd_da_5_s  =' Độ dài đường trung tuyến $AM$ của tam giác $ABC$ là $%s$'%(latex(2*dam))
            list_vd_da_5=[vd_da_5_d,vd_da_5_s]
            vd_da_5=random.choice(list_vd_da_5)

            vd_da_6_d = '\\True Độ dài đường trung tuyến $BP$ của tam giác $ABC$ là $%s$'%(latex(dbp))
            vd_da_6_s  = 'Độ dài đường trung tuyến $BP$ của tam giác $ABC$ là $%s$'%(latex(2*dbp))
            list_vd_da_6=[vd_da_6_d,vd_da_6_s]
            vd_da_6=random.choice(list_vd_da_6)

            vd_da_7_d = '\\True Độ dài đường trung tuyến $CN$ của tam giác $ABC$ là $%s$'%(latex(dcn))
            vd_da_7_s  = 'Độ dài đường trung tuyến $CN$ của tam giác $ABC$ là $%s$'%(latex(2*dcn))
            list_vd_da_7=[vd_da_7_d,vd_da_7_s]
            vd_da_7=random.choice(list_vd_da_7)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2, vd_da_3, vd_da_4, vd_da_5, vd_da_6, vd_da_7]

            # Nội dung lời giải
            loigiai_vd_1 = ('Dễ thấy $\\cos \\widehat{BAC}=\\cos \\left(\\vec{AB},\\vec{AC}\\right)$. \n'
                            'Ta có $\\vec{AB}=(%s;%s;%s)$, $\\vec{AC}=(%s;%s;%s)$.\\\\ \n' 
                            'Suy ra $\\abs{\\vec{AB}}=%s$ và $\\abs{\\vec{AC}}=%s$.\\\\ \n'
                            '\\begin{eqnarray*} \n'
                            '\\cos \\widehat{BAC}&=&\\dfrac{\\vec{AB}\\cdot\\vec{AC}}{\\abs{\\vec{AB}}\\cdot\\abs{\\vec{AC}}}\\\\'
                            '&=&\\dfrac{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}{%s\\cdot%s}=%s.\n'
                            '\\end{eqnarray*}'
                        %(latex(x2-x1),latex(y2-y1),latex(z2-z1),latex(x3-x1),latex(y3-y1),latex(z3-z1),latex(dab),latex(dac),latex(x2-x1),latex(x3-x1),latex(y2-y1),latex(y3-y1),latex(z2-z1),latex(z3-z1),latex(dab),latex(dac),latex(cosa))
                        )
            loigiai_vd_2 = ('Dễ thấy $\\cos \\widehat{ABC}=\\cos \\left(\\vec{BA},\\vec{BC}\\right)$. \n'
                            'Ta có $\\vec{BA}=(%s;%s;%s)$, $\\vec{BC}=(%s;%s;%s)$.\\\\ \n' 
                            'Suy ra $\\abs{\\vec{BA}}=%s$ và $\\abs{\\vec{BC}}=%s$.\\\\ \n'
                            '\\begin{eqnarray*} \n'
                            '\\cos \\widehat{ABC}&=&\\dfrac{\\vec{BA}\\cdot\\vec{BC}}{\\abs{\\vec{BA}}\\cdot\\abs{\\vec{BC}}}\\\\'
                            '&=&\\dfrac{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}{%s\\cdot%s}=%s.\n'
                            '\\end{eqnarray*}'
                        %(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1),latex(x3-x2),latex(y3-y2),latex(z3-z2),
                        latex(dab),latex(dbc),
                        latex(-x2+x1),latex(x3-x2),latex(-y2+y1),latex(y3-y2),latex(-z2+z1),latex(z3-z2),
                        latex(dab),latex(dbc),latex(cosb))
                        )
            loigiai_vd_3 = ('Dễ thấy $\\cos \\widehat{ACB}=\\cos \\left(\\vec{CA},\\vec{CB}\\right)$. \n'
                            'Ta có $\\vec{CA}=(%s;%s;%s)$, $\\vec{CB}=(%s;%s;%s)$.\\\\ \n' 
                            'Suy ra $\\abs{\\vec{CA}}=%s$ và $\\abs{\\vec{CB}}=%s$.\\\\ \n'
                            '\\begin{eqnarray*} \n'
                            '\\cos \\widehat{ACB}&=&\\dfrac{\\vec{CA}\\cdot\\vec{CB}}{\\abs{\\vec{CA}}\\cdot\\abs{\\vec{CB}}}\\\\'
                            '&=&\\dfrac{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}{%s\\cdot%s}=%s.\n'
                            '\\end{eqnarray*}'
                        %(latex(-x3+x1),latex(-y3+y1),latex(-z3+z1),latex(-x3+x2),latex(-y3+y2),latex(-z3+z2),latex(dac),latex(dbc),latex(-x3+x1),latex(-x3+x2),latex(-y3+y1),latex(-y3+y2),latex(-z3+z1),latex(-z3+z2),latex(dac),latex(dbc),latex(cosc))
                        )

            loigiai_vd_4 = ('Ta có $AB=\\abs{\\vec{AB}}=%s, AC=\\abs{\\vec{AC}}=%s$ và $BC=\\abs{\\vec{BC}}=%s$.\\\\ \n'
                            'Suy ra chu vi của tam giác $ABC$ là\\\\ $C_{\\Delta ABC}=AB+AC+BC=%s+%s+%s=%s$.'
                            %(latex(dab),latex(dac),latex(dbc),latex(dab),latex(dac),latex(dbc),latex(cv))
                        )
            loigiai_vd_5 = ('Toạ độ trung điểm $M$ của cạnh $BC$ là $M\\left(%s;%s;%s\\right)$.\\\\ \n'
                            'Toạ độ vectơ $\\vec{AM}=\\left(%s;%s;%s\\right)$.\\\\ \n' 
                            'Độ dài đường trung tuyến $AM$ là $AM=\\abs{\\vec{AM}}=\\sqrt{\\left(%s\\right)^2+\\left(%s\\right)^2+\\left(%s\\right)^2}=%s$.'%(latex(xm),latex(ym),latex(zm),latex(xm-x1),latex(ym-y1),latex(zm-z1),latex(xm-x1),latex(ym-y1),latex(zm-z1),latex(dam))
                        )
            loigiai_vd_6 = ('Toạ độ trung điểm $P$ của cạnh $AC$ là $P\\left(%s;%s;%s\\right)$.\\\\ \n'
                            'Toạ độ vectơ $\\vec{BP}=\\left(%s;%s;%s\\right)$.\\\\ \n' 
                            'Độ dài đường trung tuyến $BP$ là $BP=\\abs{\\vec{BP}}=\\sqrt{\\left(%s\\right)^2+\\left(%s\\right)^2+\\left(%s\\right)^2}=%s$.'%(latex(xp),latex(yp),latex(zp),latex(xp-x2),latex(yp-y2),latex(zp-z2),latex(xp-x2),latex(yp-y2),latex(zp-z2),latex(dbp))
                        )
            loigiai_vd_7 = ('Toạ độ trung điểm $N$ của cạnh $AB$ là $N\\left(%s;%s;%s\\right)$.\\\\ \n'
                            'Toạ độ vectơ $\\vec{CN}=\\left(%s;%s;%s\\right)$.\\\\ \n' 
                            'Độ dài đường trung tuyến $CN$ là $CN=\\abs{\\vec{CN}}=\\sqrt{\\left(%s\\right)^2+\\left(%s\\right)^2+\\left(%s\\right)^2}=%s$.'%(latex(xn),latex(yn),latex(zn),latex(xn-x3),latex(yn-y3),latex(zn-z3),latex(xn-x3),latex(yn-y3),latex(zn-z3),latex(dcn))
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2, loigiai_vd_3,loigiai_vd_4,loigiai_vd_5,loigiai_vd_6,loigiai_vd_7]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Nếu tứ giác giác $ABCD$ là hình bình hành với $D(x;y;z)$ thì $x+y+z=%s$'%(latex(xd+yd+zd))
            vdc_da_1_s = 'Nếu tứ giác giác $ABCD$ là hình bình hành với $D(x;y;z)$ thì $x+y+z=%s$'%(latex(-xd-yd-zd))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            vdc_da_2_d = '\\True Nếu điểm $M(x;y;z)$ thoả mãn $\\vec{AB}+%s\\vec{CM}=\\vec{0}$ thì $x+y+z=%s$'%(latex(k),latex(xi+yi+zi))
            vdc_da_2_s = 'Nếu điểm $M(x;y;z)$ thoả mãn $\\vec{AB}+%s\\vec{CM}=\\vec{0}$ thì $x+y+z=%s$'%(latex(k),latex(-xi-yi-zi))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Để tứ giác $ABCD$ là hình bình hành thì $\\vec{AD}=\\vec{BC}$.\\\\ \n'
                            'Theo bài ta có $\\vec{AD}=(x-%s;y-%s;z-%s)$ và $\\vec{BC}=(%s;%s;%s)$.\\\\ \n'
                            '$\\vec{AD}=\\vec{BC} \\Leftrightarrow \\heva{x-%s=%s\\\\y-%s=%s\\\\z-%s=%s} \\Leftrightarrow \\heva{x=%s\\\\y=%s\\\\z=%s}$.\\\\ \n'
                            'Suy ra $D(%s;%s;%s)$.\\\\ Vậy $x+y+z=%s+%s+%s=%s$.'
                            %(latex(x1),latex(y1),latex(z1),latex(x3-x2),latex(y3-y2),latex(z3-z2),latex(x1),latex(x3-x2),latex(y1),latex(y3-y2),latex(z1),latex(x3-z2),
                            latex(xd),latex(yd),latex(zd),latex(xd),latex(yd),latex(zd),latex(xd),latex(yd),latex(zd),latex(xd+yd+zd))

                        )

            loigiai_vdc_2 =  ('Dễ thấy $\\vec{AB}+%s\\vec{CM}=\\vec{0} \\Leftrightarrow \\vec{AB}=%s\\vec{CM}$.\\\\ \n'
                            'Theo bài ta có $\\vec{AB}=(%s;%s;%s)$ và $\\vec{CM}=(x-%s;y-%s;z-%s)$.\\\\ \n'
                            '$\\vec{AB}=%s\\vec{CM} \\Leftrightarrow \\heva{%s=%s(x-%s)\\\\%s=%s(y-%s)\\\\%s=%s(z-%s)} \\Leftrightarrow \\heva{x=%s\\\\y=%s\\\\z=%s}$.\\\\ \n'
                            'Suy ra $I(%s;%s;%s)$.\\\\ Vậy $x+y+z=%s+%s+%s=%s$.'
                            %(latex(k),latex(-k),latex(x2-x1),latex(y2-y1),latex(z2-z1),
                            latex(x3),latex(y3),latex(z3),latex(-k),latex(x2-x1),latex(-k),latex(x3),latex(y2-y1),latex(-k),latex(y3),latex(z2-z1),latex(-k),latex(z3),
                            latex(xi),latex(yi),latex(zi),latex(xi),latex(yi),latex(zi),latex(xi),latex(yi),latex(zi),latex(xi+yi+zi))
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('1\\vec','\\vec').replace('-1\\vec','-\\vec').replace('+-','-').replace('\\frac','\\dfrac').replace('--','+').replace('-0x','').replace('+0x','').replace('+0','').replace('-0','').replace('=0+','').replace('=0-','-').replace('+1k','+k').replace('-1k','-k').replace('+0k','').replace('-0k','').replace('=1k','=k').replace('=-1k','=-k')
            return content

