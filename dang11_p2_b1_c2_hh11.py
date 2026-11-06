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


def bt_dang11_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Khởi tạo các ký hiệu
            a_sym = symbols('a')

            # Bước 1: Random giá trị của a (chọn số chẵn để tính toán trung điểm đẹp hơn)
            val_a = random.choice([2, 4, 6, 8, 10])

            # Tính toán các đại lượng dựa trên a (sử dụng sympy để giữ biểu thức chính xác)
            # 1. NA, NB là đường cao tam giác đều cạnh a
            val_NA = (val_a * sqrt(3)) / 2
            # 2. MN là đoạn nối trung điểm hai cạnh đối của tứ diện đều
            # MN = sqrt(NA^2 - (a/2)^2) = sqrt(3a^2/4 - a^2/4) = a*sqrt(2)/2
            val_MN = (val_a * sqrt(2)) / 2
            # 3. Tích vô hướng MN.BC
            # |MN| = a*sqrt(2)/2, |BC| = a, góc = 45 độ => tích = a^2/2
            val_dot_product = Rational(val_a**2, 2)
            # 4. Góc giữa MN và BC là 45 độ


            # Nội dung câu hỏi
            noidungcauhoi = ("""Cho tứ diện đều $ABCD$ có các cạnh bằng $%s$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $CD$.
                             \\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (80.47,144.4) -- (220.47,144.4) ;
            		\\draw [line width=1]    (80.47,144.4) -- (120.47,184.4) ;
            		\\draw [line width=1]    (120.47,184.4) -- (220.47,144.4) ;
            		\\draw [line width=1]    (80.47,144.4) -- (140.47,64.4) ;
            		\\draw [line width=1]    (120.47,184.4) -- (140.47,64.4) ;
            		\\draw [line width=1]    (140.47,64.4) -- (220.47,144.4) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (110.47,104.4) -- (170.47,164.4) ;
            		\\draw (133,38) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\\draw (62,132) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\\draw (111,187) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\\draw (224,136) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\\draw (86,81) node [anchor=north west][inner sep=0.75pt]    {$M$};
            		\\draw (170.47,164.4) node [anchor=north west][inner sep=0.75pt]    {$N$};
            	\\end{tikzpicture}
            \\end{center}""" 
                             % (latex(val_a)))

            ########################################################################
            # a) Nhận biết: Kiểm tra độ dài NA, NB
            ########################################################################
            na_nb_correct = latex(val_NA)
            na_nb_wrong = latex((val_a * sqrt(3)) / 3)

            nb_da_1_d = '\\True $NA = NB = %s$' % na_nb_correct
            nb_da_1_s = '$NA = NB = %s$' % na_nb_wrong
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ("""Xét tam giác $ACD$ đều cạnh $a=%s$, $N$ là trung điểm $CD$ nên $AN$ là đường cao. \\\\
                            Do đó $AN = \\frac{%s\\sqrt{3}}{2} = %s$. Tương tự $BN = %s$.""" 
                            % (latex(val_a), latex(val_a), na_nb_correct, na_nb_correct))

            ########################################################################
            # b) Thông hiểu: Độ dài đoạn MN
            ########################################################################
            mn_correct = latex(val_MN)
            mn_wrong = latex((val_a * sqrt(3)) / 2)

            th_da_1_d = '\\True $MN = %s$' % mn_correct
            th_da_1_s = '$MN = %s$' % mn_wrong
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ("""Xét tam giác $ABN$ cân tại $N$ (vì $AN=BN$). $M$ là trung điểm $AB$ nên $NM \\perp AB$. \\\\
                            Ta có $MN = \\sqrt{AN^2 - AM^2} = \\sqrt{\\left(%s\\right)^2 - \\left(\\frac{%s}{2}\\right)^2} = %s$.""" 
                            % (na_nb_correct, latex(val_a), mn_correct))

            ########################################################################
            # c) Vận dụng: Tích vô hướng
            ########################################################################
            dot_correct = latex(val_dot_product)
            dot_wrong = latex(Rational(val_a**2, 3))

            vd_da_1_d = '\\True $\\vec{MN} \\cdot \\vec{BC} = %s$' % dot_correct
            vd_da_1_s = '$\\vec{MN} \\cdot \\vec{BC} = %s$' % dot_wrong
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ("""Gọi $P$ là trung điểm $AC$. Khi đó $MP \\parallel BC$ và $MP = \\frac{1}{2}BC = \\frac{%s}{2}$. \\\\
                            $NP \\parallel AD$ và $NP = \\frac{1}{2}AD = \\frac{%s}{2}$. \\\\
                            Ta thấy $MN^2 = \\left(%s\\right)^2 = %s$, mà $MP^2 + NP^2 = \\left(\\frac{%s}{2}\\right)^2 + \\left(\\frac{%s}{2}\\right)^2 = %s$. \\\\
                            Suy ra $\\triangle MNP$ vuông tại $P$. Góc giữa $MN$ và $BC$ (cùng hướng $MP$) là $45^\\circ$. \\\\
                            Vậy $\\vec{MN} \\cdot \\vec{BC} = MN \\cdot BC \\cdot \\cos 45^\\circ = %s \\cdot %s \\cdot \\frac{\\sqrt{2}}{2} = %s$.""" 
                            % (latex(val_a), latex(val_a), mn_correct, latex(val_MN**2), latex(val_a), latex(val_a), latex(val_MN**2), mn_correct, latex(val_a), dot_correct))

            ########################################################################
            # d) Vận dụng cao: Góc giữa hai đường thẳng
            ########################################################################
            vdc_da_1_d = '\\True Góc giữa đường thẳng $MN$ và $BC$ bằng $45^\\circ$'
            vdc_da_1_s = 'Góc giữa đường thẳng $MN$ và $BC$ bằng $60^\\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ("""Từ kết quả chứng minh $\\triangle MNP$ vuông cân tại $P$ ở câu trên, \\\\
                            ta có $\\widehat{(MN, MP)} = 45^\\circ$. Vì $MP \\parallel BC$ nên góc giữa $MN$ và $BC$ bằng $45^\\circ$.""" )

            # Logic chọn đáp án đúng/sai ngẫu nhiên
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

