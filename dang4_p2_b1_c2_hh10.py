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


def bt_dang4_p2_b1_c2_hh10(self):
            # Khai báo biến
            a=randint(2,50)

            lis1=['AB','BC','AC']
            vt1=random.choice(lis1)

            lis2=['A','B','C']
            vt2=random.choice(lis2)

            hinhve = ('\\begin{center}'
                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                '\\clip(1.7358139534883754,-0.335813953488369) rectangle (12.25488372093023,7.133953488372093);\n'
                '\\draw (4.,1.)-- (7.,6.196152422706633);\n'
                '\\draw (7.,6.196152422706633)-- (10.,1.);\n'
                '\\draw (10.,1.)-- (4.,1.);\n'
                '\\draw (7.,6.196152422706633)-- (7.,1.);\n'
                '\\draw (4.,1.)-- (8.5,3.5980762113533165);\n'
                '\\draw (6.8316279069767445,7.093023255813954) node[anchor=north west] {$A$};\n'
                '\\draw (3.4958139534883745,1.014883720930235) node[anchor=north west] {$B$};\n'
                '\\draw (10.331162790697674,1.0967441860465141) node[anchor=north west] {$C$};\n'
                '\\draw (6.872558139534884,1.014883720930235) node[anchor=north west] {$M$};\n'
                '\\draw (6.299534883720931,3.4297674418604664) node[anchor=north west] {$G$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}')
            # Nội dung câu hỏi
            noidungcauhoi = '''Cho tam giác đều $ABC$ có cạnh bằng $%s$, $M$ là trung điểm cạnh $BC$, $G$ là trọng tâm của tam giác.\n'''%(latex(a))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\left| \\overrightarrow{%s} \\right|=%s$'%(str(vt1),latex(a))
            nb_da_1_s = '$\\left| \\overrightarrow{%s} \\right|=%s$'%(str(vt1),latex(a*sqrt(2)))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Cặp vectơ $\\overrightarrow{AM}$ và $\\overrightarrow{GM}$ cùng hướng'
            nb_da_2_s = 'Cặp vectơ $\\overrightarrow{AM}$ và $\\overrightarrow{GM}$ ngược hướng'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('$\\left| \\overrightarrow{%s} \\right|=%s=%s$.'
                    %(str(vt1),str(vt1),latex(a))
                        )
            loigiai_nb_2 = ('Cặp vectơ $\\overrightarrow{AM}$ và $\\overrightarrow{GM}$ cùng hướng.'
                    )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\left| \\overrightarrow{AG} \\right|=\\dfrac{3}{2}\\left| \\overrightarrow{AM} \\right|$'
            th_da_1_s = '$\\left| \\overrightarrow{AG} \\right|=\\dfrac{2}{3}\\left| \\overrightarrow{AM} \\right|$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\left| \\overrightarrow{MG} \\right|=\\dfrac{1}{3}\\left| \\overrightarrow{AM} \\right|$'
            th_da_2_s = '$\\left| \\overrightarrow{MG} \\right|=\\dfrac{2}{3}\\left| \\overrightarrow{AM} \\right|$'
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('$\\left| \\overrightarrow{AG} \\right|=\\dfrac{3}{2}\\left| \\overrightarrow{AM} \\right|$.'
                        )
            loigiai_th_2 = ('$\\left| \\overrightarrow{MG} \\right|=\\dfrac{1}{3}\\left| \\overrightarrow{AM} \\right|$.'
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
            vd_da_1_d = '\\True $\\left| \\overrightarrow{AM} \\right|=%s$' %(latex(a*sqrt(3)/2))
            vd_da_1_s = '$\\left| \\overrightarrow{AM} \\right|=%s$' %(latex(a*sqrt(3)/4))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $\\left| \\overrightarrow{AM} \\right|=%s$' %(latex(a*sqrt(3)/2))
            vd_da_2_s = '$\\left| \\overrightarrow{AM} \\right|=%s$' %(latex(a*sqrt(2)/3))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Tam giác $ABC$ đều cạnh $%s$ nên $AM=\\dfrac{%s \\sqrt{3}}{2}=%s$. \\\\ \n'
                    'Vậy độ dài vectơ $\\overrightarrow{AM}$ là $%s$.'
                    %(latex(a),latex(a),latex(a*sqrt(3)/2),
                    latex(a*sqrt(3)/2),
                    )
                        )
            loigiai_vd_2 = ('Tam giác $ABC$ đều cạnh $%s$ nên $AM=\\dfrac{%sa \\sqrt{3}}{2}=%s$. \\\\ \n'
                    'Vậy độ dài vectơ $\\overrightarrow{AM}$ là $%s$.'
                    %(latex(a),latex(a),latex(a*sqrt(3)/2),
                    latex(a*sqrt(3)/2),
                    )
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $\\left| \\overrightarrow{%sG} \\right|=%s$' %(str(vt2),latex(a*sqrt(3)/3))
            vdc_da_1_s = '$\\left| \\overrightarrow{%sG} \\right|=%s$' %(str(vt2),latex(a*sqrt(3)/4))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True $\\left| \\overrightarrow{%sG} \\right|=%s$' %(str(vt2),latex(a*sqrt(3)/3))
            vdc_da_2_s = '$\\left| \\overrightarrow{%sG} \\right|=%s$' %(str(vt2),latex(a*sqrt(2)/6))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('$M$ là trung điểm của $BC$. \\\\ \n'
                    'Tam giác $ABC$ đều cạnh $%s$ nên $AM=\\dfrac{%s \\sqrt{3}}{2}=%s$. \\\\ \n'
                    'Suy ra $%sG=\\dfrac{2}{3}AM =\\dfrac{2}{3} \\cdot %s =%s$. \\\\ \n'
                    'Vậy độ dài vectơ $\\overrightarrow{%sG}$ là $%s$.'
                    %(latex(a),latex(a),latex(a*sqrt(3)/2),
                    str(vt2), latex(a*sqrt(3)/2), latex(a*sqrt(3)/3),
                    str(vt2),latex(a*sqrt(3)/3),
                    ))
            loigiai_vdc_2 = ('$M$ là trung điểm của $BC$. \\\\ \n'
                    'Tam giác $ABC$ đều cạnh $%s$ nên $AM=\\dfrac{%s \\sqrt{3}}{2}=%s$. \\\\ \n'
                    'Suy ra $%sG=\\dfrac{2}{3}AM =\\dfrac{2}{3} \\cdot %s =%s$. \\\\ \n'
                    'Vậy độ dài vectơ $\\overrightarrow{%sG}$ là $%s$.'
                    %(latex(a),latex(a),latex(a*sqrt(3)/2),
                    str(vt2), latex(a*sqrt(3)/2), latex(a*sqrt(3)/3),
                    str(vt2),latex(a*sqrt(3)/3),
                    ))
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
                '\\loigiai{\n'+hinhve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

