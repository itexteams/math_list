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


def bt_dang30_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random các thông số cho bài toán
            # tA: thời gian sx sản phẩm A (giờ)
            tA = random.randint(2, 5)
            # tB: thời gian sx sản phẩm B (giờ)
            tB = random.randint(2, 5)
            while tA == tB or math.gcd(tA, tB) != 1:
                tB = random.randint(2, 5)

            # T: Thời gian tối đa (giờ)
            # Để có nghiệm đẹp, lấy T là bội của tA và tB
            T_base = random.randint(10, 25)
            T = T_base * tA * tB

            # Random cho câu c (VD)
            # Một bộ nghiệm (x, y) thỏa mãn tA*x + tB*y <= T
            x_true = random.randint(1, (T // tA) - 2)
            y_true = random.randint(1, (T - tA * x_true) // tB)

            # Một bộ nghiệm (x, y) KHÔNG thỏa mãn tA*x + tB*y <= T
            x_false = random.randint((T // tA) + 1, (T // tA) + 10)
            y_false = random.randint((T // tB) + 1, (T // tB) + 10)


            # Nội dung câu hỏi
            noidungcauhoi = ('''Một nhà máy sản xuất hai loại sản phẩm: sản phẩm $A$ và sản phẩm $B$. Thời gian sản xuất sản phẩm $A$ là $%s$ giờ và sản phẩm $B$ là $%s$ giờ. Nhà máy có tối đa $%s$ giờ sản xuất mỗi tuần.'''                  
                             % (tA, tB, T))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Thời gian sản xuất sản phẩm $A$ có thể là $%sx$ và thời gian sản xuất sản phẩm $B$ có thể là $%sy$, điều kiện $x, y \\in \\mathbb{N}$' % (tA, tB)
            nb_da_1_s = 'Thời gian sản xuất sản phẩm $A$ có thể là $%sx$ và thời gian sản xuất sản phẩm $B$ có thể là $%sy$, điều kiện $x, y \\in \\mathbb{R}$' % (tA, tB)

            loigiai_nb_d = ('''Gọi $x, y$ lần lượt là số sản phẩm $A$ và $B$ được sản xuất ($x, y \\in \\mathbb{N}$). \\\\ 
            Khi đó thời gian sản xuất sản phẩm $A$ là $%sx$ và thời gian sản xuất sản phẩm $B$ là $%sy$. \\\\ 
            Mệnh đề đúng.''' % (tA, tB))

            loigiai_nb_s = ('''Gọi $x, y$ lần lượt là số sản phẩm $A$ và $B$ được sản xuất ($x, y \\in \\mathbb{N}$ vì số sản phẩm phải là số tự nhiên). \\\\ 
            Khi đó thời gian sản xuất sản phẩm $A$ là $%sx$ và thời gian sản xuất sản phẩm $B$ là $%sy$. \\\\ 
            Mệnh đề sai vì điều kiện của $x,y$ là $x,y \\in \\mathbb{N}$, không phải $\\mathbb{R}$.''' % (tA, tB))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Bất phương trình cho hai ẩn $x, y$ là $%sx + %sy \\le %s$' % (tA, tB, T)
            th_da_1_s = 'Bất phương trình cho hai ẩn $x, y$ là $%sx + %sy \\ge %s$' % (tA, tB, T)

            loigiai_th_d = ('''Tổng thời gian sản xuất hai sản phẩm là $%sx + %sy$ (giờ). \\\\
            Vì nhà máy có tối đa $%s$ giờ sản xuất mỗi tuần nên ta có bất phương trình: $%sx + %sy \\le %s$. \\\\
            Mệnh đề đúng.''' % (tA, tB, T, tA, tB, T))

            loigiai_th_s = ('''Tổng thời gian sản xuất hai sản phẩm là $%sx + %sy$ (giờ). \\\\
            Vì nhà máy có tối đa $%s$ giờ sản xuất mỗi tuần nên ta có bất phương trình: $%sx + %sy \\le %s$. \\\\
            Mệnh đề sai.''' % (tA, tB, T, tA, tB, T))

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Nhà máy có thể sản xuất $%s$ sản phẩm loại $A$ và $%s$ sản phẩm loại $B$' % (x_true, y_true)
            vd_da_1_s = 'Nhà máy có thể sản xuất $%s$ sản phẩm loại $A$ và $%s$ sản phẩm loại $B$' % (x_false, y_false)

            val_true = tA * x_true + tB * y_true
            val_false = tA * x_false + tB * y_false

            loigiai_vd_d = ('''Thay $x = %s, y = %s$ vào bất phương trình $%sx + %sy \\le %s$, ta được: \\\\
            $%s \\cdot %s + %s \\cdot %s = %s \\le %s$ (đúng). \\\\
            Vậy nhà máy có thể sản xuất được. \\\\
            Mệnh đề đúng.''' % (x_true, y_true, tA, tB, T, tA, x_true, tB, y_true, val_true, T))

            loigiai_vd_s = ('''Thay $x = %s, y = %s$ vào bất phương trình $%sx + %sy \\le %s$, ta được: \\\\
            $%s \\cdot %s + %s \\cdot %s = %s \\le %s$ (sai, vì $%s > %s$). \\\\
            Vậy nhà máy không thể sản xuất số lượng này. \\\\
            Mệnh đề sai.''' % (x_false, y_false, tA, tB, T, tA, x_false, tB, y_false, val_false, T, val_false, T))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Miền nghiệm của bất phương trình $%sx + %sy \\le %s$ là nửa mặt phẳng bờ là đường thẳng $%sx + %sy = %s$ chứa gốc tọa độ $O(0;0)$' % (tA, tB, T, tA, tB, T)
            vdc_da_1_s = 'Miền nghiệm của bất phương trình $%sx + %sy \\le %s$ là nửa mặt phẳng bờ là đường thẳng $%sx + %sy = %s$ không chứa gốc tọa độ $O(0;0)$' % (tA, tB, T, tA, tB, T)


            loigiai_vdc_d = ('''Đường thẳng $d: %sx + %sy = %s$ chia mặt phẳng tọa độ thành hai nửa mặt phẳng. \\\\
            Thay tọa độ điểm $O(0;0)$ vào vế trái bất phương trình, ta có: $%s \\cdot 0 + %s \\cdot 0 = 0 \\le %s$ (đúng). \\\\
            Vậy miền nghiệm của bất phương trình là nửa mặt phẳng bờ $d$ chứa gốc tọa độ $O(0;0)$ (kể cả bờ $d$). \\\\
            Mệnh đề đúng.''' % (tA, tB, T, tA, tB, T))

            loigiai_vdc_s = ('''Đường thẳng $d: %sx + %sy = %s$ chia mặt phẳng tọa độ thành hai nửa mặt phẳng. \\\\
            Thay tọa độ điểm $O(0;0)$ vào vế trái bất phương trình, ta có: $%s \\cdot 0 + %s \\cdot 0 = 0 \\le %s$ (đúng). \\\\
            Vậy miền nghiệm của bất phương trình là nửa mặt phẳng bờ $d$ chứa gốc tọa độ $O(0;0)$ (kể cả bờ $d$). \\\\
            Mệnh đề sai.''' % (tA, tB, T, tA, tB, T))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Gom nhóm phương án và lời giải để đồng bộ logic khi xáo trộn
            list_nb = [(nb_da_1_d, loigiai_nb_d), (nb_da_1_s, loigiai_nb_s)]
            list_th = [(th_da_1_d, loigiai_th_d), (th_da_1_s, loigiai_th_s)]
            list_vd = [(vd_da_1_d, loigiai_vd_d), (vd_da_1_s, loigiai_vd_s)]
            list_vdc = [(vdc_da_1_d, loigiai_vdc_d), (vdc_da_1_s, loigiai_vdc_s)]

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb = random.choice(list_nb)
                th = random.choice(list_th)
                vd = random.choice(list_vd)
                vdc = random.choice(list_vdc)

                answers = [nb[0], th[0], vd[0], vdc[0]]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (Đảm bảo câu hỏi đi kèm đúng với lời giải tương ứng)
            list_nb_1 = [nb[0]]
            list_nb_2 = [nb[1]]

            list_th_1 = [th[0]]
            list_th_2 = [th[1]]

            list_vd_1 = [vd[0]]
            list_vd_2 = [vd[1]]

            list_vdc_1 = [vdc[0]]
            list_vdc_2 = [vdc[1]]

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
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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

