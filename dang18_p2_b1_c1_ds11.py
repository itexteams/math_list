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


def bt_dang18_p2_b1_c1_ds11(self):
    # Chuỗi vẽ hình TikZ đường tròn lượng giác gốc A, hình vuông M1M2M3M4
    tikz_image = ('''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                \\draw  [line width=1]  (93.4,146.8) .. controls (93.4,106.59) and (125.99,74) .. (166.2,74) .. controls (206.41,74) and (239,106.59) .. (239,146.8) .. controls (239,187.01) and (206.41,219.6) .. (166.2,219.6) .. controls (125.99,219.6) and (93.4,187.01) .. (93.4,146.8) -- cycle ;
                \\draw [line width=1]    (68,146.8) -- (271,146.8) ;
                \\draw [shift={(275,146.8)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                \\draw [line width=1]    (166.2,242.6) -- (166.2,41.6) ;
                \\draw [shift={(166.2,37.6)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                \\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (114,97.6) -- (218.7,199.3) ;
                \\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (114,196.6) -- (217,93.6) ;
                \\draw (259,122) node [anchor=north west][inner sep=0.75pt]    {$x$};
                \\draw (146,36) node [anchor=north west][inner sep=0.75pt]    {$y$};
                \\draw (147,152) node [anchor=north west][inner sep=0.75pt]    {$O$};
                \\draw (218.7,199.3) node [anchor=north west][inner sep=0.75pt]    {$M_{1}$};
                \\draw (217,70) node [anchor=north west][inner sep=0.75pt]    {$M_{2}$};
                \\draw (81,74) node [anchor=north west][inner sep=0.75pt]    {$M_{3}$};
                \\draw (84,195) node [anchor=north west][inner sep=0.75pt]    {$M_{4}$};
                \\draw (239,146.8) node [anchor=north west][inner sep=0.75pt]    {$A$};
                \\draw (169,54) node [anchor=north west][inner sep=0.75pt]    {$B$};
                \\draw (67,125) node [anchor=north west][inner sep=0.75pt]    {$A'$};
                \\draw (166.2,219.6) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            \\end{tikzpicture}''')

    # Nội dung câu hỏi sử dụng định dạng %s theo yêu cầu mẫu
    noidungcauhoi = ('''\\immini{Hình vẽ bên là vòng tròn lượng giác gốc $A$, trong đó $M_1M_2M_3M_4$ là hình vuông, $\\widehat{AOM_1} = 45^\\circ$. Xét góc lượng giác $\\alpha$ có điểm đầu là điểm $A$, điểm cuối là điểm bất kỳ nào đó trên vòng tròn lượng giác.}{%s}''' % tikz_image)

    ########################################################################
    # Nhận biết ############################################
    nb_da_1_d = '\\True Tại điểm cuối $B$ thì $\\sin \\alpha = 1$'
    nb_da_1_s = 'Tại điểm cuối $B$ thì $\\sin \\alpha = 0$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Tại điểm cuối $B$, góc lượng giác $\\alpha = 90^\\circ + k360^\\circ$ nên $\\sin \\alpha = 1$.''')
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu (ĐÃ ĐƯỢC SỬA LỖI) ##########################
    # Tạo sẵn 1 phương án đúng và 1 phương án sai để tương thích với thuật toán random cân bằng ở cuối
    th_da_1_d = '\\True Tại điểm cuối $M_3$ thì $\\sin \\alpha + 4\\cos \\alpha < 0$'
    th_da_1_s = 'Tại điểm cuối $M_3$ thì $4\\sin \\alpha + \\cos \\alpha < 0$'

    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    # Lời giải chung cho cả phương án đúng và sai
    loigiai_th_1 = ('''Tại điểm cuối $M_3$, góc lượng giác $\\alpha = 135^\\circ + k360^\\circ$.\\\\
    Khi đó $\\sin \\alpha = \\frac{\\sqrt{2}}{2}$ và $\\cos \\alpha = -\\frac{\\sqrt{2}}{2}$.\\\\
    Ta có $\\sin \\alpha + 4\\cos \\alpha = -\\frac{3\\sqrt{2}}{2} < 0$ và $4\\sin \\alpha + \\cos \\alpha = \\frac{3\\sqrt{2}}{2} > 0$.''')

    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## 
    # Vận dụng ############################################
    vd_da_1_d = '\\True Hai điểm $M_2, M_3$ là điểm biểu diễn đầy đủ nghiệm của phương trình lượng giác $\\sin x = \\frac{\\sqrt{2}}{2}$'
    vd_da_1_s = 'Hai điểm $M_2, M_3$ là điểm biểu diễn đầy đủ nghiệm của phương trình lượng giác $\\sin x = -\\frac{\\sqrt{2}}{2}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Phương trình $\\sin x = \\frac{\\sqrt{2}}{2}$ có các họ nghiệm là $x = 45^\\circ + k360^\\circ$ (biểu diễn bởi $M_2$) và $x = 135^\\circ + k360^\\circ$ (biểu diễn bởi $M_3$).''')
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## 
    # Vận dụng cao ############################################
    vdc_da_1_d = '\\True Khi di chuyển điểm cuối $M_1 \\rightarrow M_2$ thì $\\tan \\alpha$ tăng liên tục từ $-1$ đến $1$'
    vdc_da_1_s = 'Khi di chuyển điểm cuối $M_1 \\rightarrow M_2$ thì $\\tan \\alpha$ giảm dần'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Khi di chuyển từ $M_1$ (ứng với $-45^\\circ$) đến $M_2$ (ứng với $45^\\circ$), góc $\\alpha$ tăng liên tục trong khoảng $\\left(-45^\\circ; 45^\\circ\\right)$.\\\\
    Hàm số $y = \\tan \\alpha$ đồng biến trên khoảng này, do đó $\\tan \\alpha$ tăng dần từ $-1$ đến $1$.''')
    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1) # BÂY GIỜ ĐÃ CÓ list_th_da_1 ĐỂ LẶP
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
    str(noidungcauhoi)+ '\n'
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

