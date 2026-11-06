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


def bt_dang7_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tứ diện $OABC$ có $OA, OB, OC$ đôi một vuông góc với nhau. Gọi $H$ là hình chiếu của $O$ trên $\\left( ABC \\right)$.''')

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án cho mệnh đề (a)
            nb_da_1_d = '\\True $BC \\perp \\left( AOH \\right)$'
            nb_da_1_s = '$BC \\perp \\left( ABC \\right)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Nội dung lời giải chi tiết
            loigiai_nb_1 = ('''Ta có $OA \\perp OB$ và $OA \\perp OC \\Rightarrow OA \\perp \\left( OBC \\right) \\Rightarrow OA \\perp BC$. \\\\
                            Mặt khác, $OH \\perp \\left( ABC \\right) \\Rightarrow OH \\perp BC$. \\\\
                            Từ đó suy ra $BC \\perp \\left( AOH \\right)$.''')

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án cho mệnh đề (b)
            th_da_1_d = '\\True $\\frac{1}{OH^2} = \\frac{1}{OA^2} + \\frac{1}{OB^2} + \\frac{1}{OC^2}$'
            th_da_1_s = '$\\frac{1}{OH} = \\frac{1}{OA} + \\frac{1}{OB} + \\frac{1}{OC}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Gọi $K$ là giao điểm của $AH$ và $BC$. Vì $BC \\perp \\left( AOH \\right) \\Rightarrow BC \\perp AK$. \\\\
                            Trong tam giác vuông $OBC$, ta có $\\frac{1}{OK^2} = \\frac{1}{OB^2} + \\frac{1}{OC^2}$. \\\\
                            Trong tam giác vuông $OAK$, ta có $\\frac{1}{OH^2} = \\frac{1}{OA^2} + \\frac{1}{OK^2} = \\frac{1}{OA^2} + \\frac{1}{OB^2} + \\frac{1}{OC^2}$.''')

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án cho mệnh đề (c)
            vd_da_1_d = '\\True $H$ là trực tâm $\\triangle ABC$'
            vd_da_1_s = '$H$ là trọng tâm $\\triangle ABC$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Từ $BC \\perp \\left( AOH \\right) \\Rightarrow BC \\perp AH$. \\\\
                            Chứng minh tương tự ta có $AC \\perp BH$. \\\\
                            Vậy $H$ là trực tâm của tam giác $ABC$.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án cho mệnh đề (d)
            vdc_da_1_d = '$AH \\perp \\left( OBC \\right)$' # Mệnh đề sai
            vdc_da_1_s = '\\True $OA \\perp \\left( OBC \\right)$' # Mệnh đề đúng
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $OA \\perp OB$ và $OA \\perp OC$ nên $OA \\perp \\left( OBC \\right)$. \\\\
                            Nếu $AH \\perp \\left( OBC \\right)$ thì $AH \\parallel OA$ (vô lý vì $A$ là điểm chung và $O$ không nằm trên mặt phẳng $\\left( ABC \\right)$).''')

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm soát số lượng đáp án đúng (từ 1 đến 3)
            while True:
                a_ans = random.choice(list_nb_da_1)
                b_ans = random.choice(list_th_da_1)
                c_ans = random.choice(list_vd_da_1)
                d_ans = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([a_ans, b_ans, c_ans, d_ans]) <= 3:
                    break

            # Hình vẽ TikZ
            hinh_ve = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,139.69) -- (103.47,30.4) ;
            		\draw [line width=1]    (103.47,139.69) -- (169.04,183.4) ;
            		\draw [line width=1]    (169.04,183.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (169.04,183.4) ; 
            		\draw [line width=1]    (129.47,90.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (208.38,168.1) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (155.92,99.25) -- (103.47,139.69) ;
            		\draw (83,128) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (160,190) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (283,128) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (95,5) node [anchor=north west][inner sep=0.75pt]    {$S$};
            		\draw (156,79) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\draw (208.38,168.1) node [anchor=north west][inner sep=0.75pt]    {$I$};
            	\end{tikzpicture}
            \end{center}''')

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) +
                '\\choiceTFn \n'
                '{' + str(a_ans) + '}\n'
                '{' + str(b_ans) + '}\n'
                '{' + str(c_ans) + '}\n'
                '{' + str(d_ans) + '}\n'
                '\\loigiai{ \n'
                +hinh_ve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

