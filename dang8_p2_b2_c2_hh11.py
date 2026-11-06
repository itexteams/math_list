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


def bt_dang8_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Random cạnh của tam giác đều ABC là x
            x = random.choice([2, 3, 4, 6]) 
            # Random hệ số của SA = k*sqrt(2). Ở đề bài gốc là 3*sqrt(2)
            k = random.choice([2, 3, 5]) 

            # Tính toán các đại lượng
            # AM là đường cao tam giác đều cạnh x: AM = x*sqrt(3)/2
            am_sq = Rational(3 * x**2, 4)
            sa_sq = 2 * k**2
            # AH^2 = (SA^2 * AM^2) / (SA^2 + AM^2)
            ah_sq = (sa_sq * am_sq) / (sa_sq + am_sq)
            ah_val = simplify(sqrt(ah_sq))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $%s$. Biết $SA=%s\\sqrt{2}$ và $SA$ vuông góc với mặt đáy. Gọi $M$ là trung điểm của $BC$ và $H$ là hình chiếu vuông góc của $A$ lên $SM$.''' 
                             %(latex(x), latex(k)))

            # --- Vẽ hình TikZ ---
            ve_hinh = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,139.69) -- (103.47,30.4) ;
            		\draw [line width=1]    (103.47,139.69) -- (169.04,183.4) ;
            		\draw [line width=1]    (169.04,183.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (169.04,183.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (223.68,161.54) ;
            		\draw [line width=1]    (103.47,30.4) -- (223.68,161.54) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (155.47,87.4) -- (103.47,139.69) ;
            		\draw (83,128) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (160,190) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (283,128) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (95,5) node [anchor=north west][inner sep=0.75pt]    {$S$};
            		\draw (155,72) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\draw (223.68,161.54) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\end{tikzpicture}
            \end{center}''')

            ########################################################################
            # (a) Nhận biết: BC vuông góc AH
            nb_da_1_d = '\\True Đường thẳng $BC$ vuông góc với đường thẳng $AH$'
            nb_da_1_s = 'Đường thẳng $BC$ song song với đường thẳng $AH$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta có $BC \\perp AM$ (do tam giác $ABC$ đều) và $BC \\perp SA$ (do $SA \\perp (ABC)$). Suy ra $BC \\perp (SAM)$. Vì $AH \\subset (SAM)$ nên $BC \\perp AH$.''')

            ########################################################################
            # (b) Thông hiểu: AH vuông góc (SBC)
            th_da_1_d = '\\True Đường thẳng $AH$ vuông góc với mặt phẳng $(SBC)$'
            th_da_1_s = 'Đường thẳng $AH$ song song với mặt phẳng $(SBC)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Theo chứng minh trên $AH \\perp BC$. Lại có $AH \\perp SM$ (giả thiết). Mà $BC, SM \\subset (SBC)$ nên $AH \\perp (SBC)$.''')

            ########################################################################
            # (c) Vận dụng: SH là hình chiếu của SA trên (SBC)
            vd_da_1_d = '\\True Đường thẳng $SH$ là hình chiếu của đường thẳng $SA$ lên mặt phẳng $(SBC)$'
            vd_da_1_s = 'Đường thẳng $SB$ là hình chiếu của đường thẳng $SA$ lên mặt phẳng $(SBC)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $AH \\perp (SBC)$ nên $H$ là hình chiếu của $A$ lên $(SBC)$. Lại có $S \\in (SBC)$ nên $SH$ là hình chiếu vuông góc của $SA$ lên mặt phẳng $(SBC)$.''')

            ########################################################################
            # (d) Vận dụng cao: Độ dài AH
            # Tính giá trị sai (lấy giá trị 18/11 hoặc đảo tử mẫu)
            sai_val = Rational(18, 11) if ah_val != Rational(18, 11) else Rational(11, 18)
            vdc_da_1_d = '\\True Độ dài đoạn thẳng $AH$ bằng $%s$' %(latex(ah_val))
            vdc_da_1_s = 'Độ dài đoạn thẳng $AH$ bằng $%s$' %(latex(sai_val))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Tam giác $SAM$ vuông tại $A$ có $AH$ là đường cao. Ta có $AM = \\frac{%s\\sqrt{3}}{2}$. \\\\ $AH = \\frac{SA \\cdot AM}{\\sqrt{SA^2+AM^2}} = \\frac{%s\\sqrt{2} \\cdot \\frac{%s\\sqrt{3}}{2}}{\\sqrt{(%s\\sqrt{2})^2 + (\\frac{%s\\sqrt{3}}{2})^2}} = %s$.''' 
                             %(latex(x), latex(k), latex(x), latex(k), latex(x), latex(ah_val)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Gán lại giá trị đã chọn
            final_ans = [ans_a, ans_b, ans_c, ans_d]
            final_sol = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +
                '\\choiceTFn \n'
                '{' + str(final_ans[0]) + '}\n'
                '{' + str(final_ans[1]) + '}\n'
                '{' + str(final_ans[2]) + '}\n'
                '{' + str(final_ans[3]) + '}\n'
                '\\loigiai{ \n'
                + str(ve_hinh) +
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_sol[0]) + '\n'
                '\\item ' + str(final_sol[1]) + '\n'
                '\\item ' + str(final_sol[2]) + '\n'
                '\\item ' + str(final_sol[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

