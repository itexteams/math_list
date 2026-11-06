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


def bt_dang1_p2_b3_c2_hh10(self):
            # Khai báo biến
            a=randint(2,5)

            # Nội dung câu hỏi
            noidungcauhoi = 'Cho tam giác $ABC$ có $G$ là trọng tâm. Gọi $D$ là điểm đối xứng của $B$ qua $G$, $M$ là trung điểm của $BC$.'

            hinhve=(
                    '\\begin{center}  \n'
                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                    '\\clip(-0.7696015292127467,-0.9605618223132615) rectangle (5.496719791677505,3.8658878715341944); \n'
                    '\\draw [line width=1.pt] (0.,0.)-- (2.,3.); \n'
                    '\\draw [line width=1.pt] (2.,3.)-- (5.,0.); \n'
                    '\\draw [line width=1.pt] (5.,0.)-- (0.,0.); \n'
                    '\\draw [line width=1.pt] (2.,3.)-- (2.5,0.); \n'
                    '\\draw [line width=1.pt] (0.,0.)-- (3.5,1.5); \n'
                    '\\draw [line width=1.pt] (2.3333333333333335,1.)-- (4.666666666666667,2.); \n'
                    '\\draw [line width=1.pt] (4.666666666666667,2.)-- (2.,3.); \n'
                    '\\draw [line width=1.pt] (4.666666666666667,2.)-- (5.,0.); \n'
                    '\\draw [line width=1.pt] (4.666666666666667,2.)-- (2.5,0.); \n'
                    '\\draw (1.7645725343825756,3.6) node[anchor=north west] {A}; \n'
                    '\\draw (-0.377956446657106,-0.0966388460875832) node[anchor=north west] {B}; \n'
                    '\\draw (5.070517790072837,-0.18879063021832224) node[anchor=north west] {C}; \n'
                    '\\draw (4.74798654561525,2.287788568295289) node[anchor=north west] {D}; \n'
                    '\\draw (2.2,-0.2) node[anchor=north west] {M}; \n'
                    '\\draw (1.6,1.4) node[anchor=north west] {G}; \n'
                '\\end{tikzpicture}  \n' 
                '\\end{center} \n'
                    )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\vec{MD}=\\vec{MG}+\\vec{GD}$'
            nb_da_1_s = '$\\vec{DM}=\\vec{MG}+\\vec{GD}$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $\\vec{GA}=-2\\vec{GM}$'
            nb_da_2_s = '$\\vec{GA}=2\\vec{GM}$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Theo quy tắc ba điểm, ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{MG}+\\vec{GD}=\\vec{MD}$.'
                        )
            loigiai_nb_2 = ('Từ tính chất trọng tâm, ta có $\\vec{GA}=-2\\vec{GM}$.'
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
            th_da_1_d = '\\True $\\vec{AG}=\\dfrac{1}{3} \\vec{AB}+\\dfrac{1}{3} \\vec{AC}$'
            th_da_1_s = '$\\vec{AG}=%s \\vec{AB}+\\dfrac{1}{3} \\vec{AC}$' %(latex(a))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{AG}=\\dfrac{2}{3} \\vec{AM}=\\dfrac{1}{3} \\cdot 2 \\vec{AM}=\\dfrac{1}{3} \\left( \\vec{AB} +\\vec{AC} \\right) = \\dfrac{1}{3} \\vec{AB} +\\dfrac{1}{3}\\vec{AC}$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $\\vec{CD}=2\\vec{BG}-2\\vec{BM}$'
            vd_da_1_s = '$\\vec{CD}=\\vec{BG}+\\vec{BM}$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{CD}=\\vec{CB}+\\vec{BD}=2 \\vec{CM}+2\\vec{BG}=2 \\vec{MB}+2\\vec{BG}=2\\vec{BG}-2\\vec{BM}$.'
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
            vdc_da_1_d = '\\True $\\vec{AM}=\\frac{1}{2} \\vec{AB}+\\frac{1}{2} \\vec{AC}$'
            vdc_da_1_s = '$\\vec{AM}=\\frac{3}{2} \\vec{AB}+\\frac{1}{2} \\vec{AC}$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải

            loigiai_vdc_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{AM}=\\vec{AB}+\\vec{BM}=\\vec{AB}+\\frac{1}{2} \\vec{BC}=\\vec{AB}+\\frac{1}{2} \\vec{BA}+\\frac{1}{2} \\vec{AC}$ \\\\ \n'
                            '\\hspace*{1.9cm} $=\\vec{AB}-\\frac{1}{2} \\vec{AB}+\\frac{1}{2} \\vec{AC}=\\frac{1}{2} \\vec{AB}+\\frac{1}{2} \\vec{AC}$.'
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

