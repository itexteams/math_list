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


def bt_dang28_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và random thông số
            a = random.randint(2, 6)

            # Điểm M đúng (thỏa mãn x + y <= a)
            xM_true = random.randint(0, a - 1)
            yM_true = random.randint(0, a - xM_true)

            # Điểm M sai (không thỏa mãn x + y <= a)
            xM_false = random.randint(a + 1, a + 4)
            yM_false = random.randint(a + 1, a + 4)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho bất phương trình $x \\le %s - y$. $(1)$''' % a)

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Bất phương trình $(1)$ là bất phương trình bậc nhất hai ẩn'
            nb_da_1_s = 'Bất phương trình $(1)$ không phải là bất phương trình bậc nhất hai ẩn'

            loigiai_nb_d = ('''Bất phương trình $(1)$ có thể viết lại thành $x + y \\le %s$. Đây là bất phương trình bậc nhất hai ẩn dạng $ax+by \\le c$ với $a=1, b=1, c=%s$. \\\\ 
            Mệnh đề đúng.''' % (a, a))
            loigiai_nb_s = ('''Bất phương trình $(1)$ có thể viết lại thành $x + y \\le %s$. Đây là bất phương trình bậc nhất hai ẩn dạng $ax+by \\le c$ với $a=1, b=1, c=%s$. \\\\ 
            Mệnh đề sai.''' % (a, a))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Điểm $M(%s;%s)$ thuộc miền nghiệm của bất phương trình $(1)$' % (xM_true, yM_true)
            th_da_1_s = 'Điểm $M(%s;%s)$ thuộc miền nghiệm của bất phương trình $(1)$' % (xM_false, yM_false)

            loigiai_th_d = ('''Thay tọa độ điểm $M(%s;%s)$ vào bất phương trình $(1)$ ta được: \\\\
            $%s \\le %s - %s \\Leftrightarrow %s \\le %s$ (luôn đúng). \\\\
            Vậy điểm $M$ thuộc miền nghiệm của bất phương trình $(1)$. \\\\
            Mệnh đề đúng.''' % (xM_true, yM_true, xM_true, a, yM_true, xM_true, a - yM_true))
            loigiai_th_s = ('''Thay tọa độ điểm $M(%s;%s)$ vào bất phương trình $(1)$ ta được: \\\\
            $%s \\le %s - %s \\Leftrightarrow %s \\le %s$ (vô lý). \\\\
            Vậy điểm $M$ không thuộc miền nghiệm của bất phương trình $(1)$. \\\\
            Mệnh đề sai.''' % (xM_false, yM_false, xM_false, a, yM_false, xM_false, a - yM_false))

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Với $y=0$ thì có $%s$ giá trị nguyên dương của $x$ để thoả mãn bất phương trình $(1)$' % a
            vd_da_1_s = 'Với $y=0$ thì có $%s$ giá trị nguyên dương của $x$ để thoả mãn bất phương trình $(1)$' % (a + 1)

            if a == 2:
                set_x = '\\{1; 2\\}'
            elif a == 3:
                set_x = '\\{1; 2; 3\\}'
            else:
                set_x = '\\{1; 2; ...; %s\\}' % a

            loigiai_vd_d = ('''Với $y=0$, bất phương trình $(1)$ trở thành $x \\le %s$. \\\\
            Vì $x$ là số nguyên dương nên $x \\in %s$. \\\\
            Vậy có $%s$ giá trị nguyên dương của $x$ thỏa mãn. \\\\
            Mệnh đề đúng.''' % (a, set_x, a))
            loigiai_vd_s = ('''Với $y=0$, bất phương trình $(1)$ trở thành $x \\le %s$. \\\\
            Vì $x$ là số nguyên dương nên $x \\in %s$. \\\\
            Vậy có $%s$ giá trị nguyên dương của $x$ thỏa mãn. \\\\
            Mệnh đề sai.''' % (a, set_x, a))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Bất phương trình $(1)$ có miền nghiệm là nửa mặt phẳng bờ là đường thẳng $\\Delta$ thì $\\Delta$ tạo với $2$ trục tọa độ thành một tam giác vuông cân'
            vdc_da_1_s = 'Bất phương trình $(1)$ có miền nghiệm là nửa mặt phẳng bờ là đường thẳng $\\Delta$ thì $\\Delta$ tạo với $2$ trục tọa độ thành một tam giác đều'

            loigiai_vdc_d = ('''Bất phương trình $(1)$ tương đương với $x + y - %s \\le 0$. \\\\
            Đường thẳng $\\Delta: x + y - %s = 0$ cắt trục $Ox$ tại $A(%s;0)$ và cắt trục $Oy$ tại $B(0;%s)$. \\\\
            Tam giác $OAB$ vuông tại $O$ và có $OA = OB = %s$ nên tam giác $OAB$ là tam giác vuông cân. \\\\
            Mệnh đề đúng.''' % (a, a, a, a, a))
            loigiai_vdc_s = ('''Bất phương trình $(1)$ tương đương với $x + y - %s \\le 0$. \\\\
            Đường thẳng $\\Delta: x + y - %s = 0$ cắt trục $Ox$ tại $A(%s;0)$ và cắt trục $Oy$ tại $B(0;%s)$. \\\\
            Tam giác $OAB$ vuông tại $O$ và có $OA = OB = %s$ nên tam giác $OAB$ là tam giác vuông cân. \\\\
            Mệnh đề sai.''' % (a, a, a, a, a))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Gom nhóm phương án và lời giải
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

            # Gán lại vào list
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

