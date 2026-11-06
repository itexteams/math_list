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


def bt_dang13_p2_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            # n1_g: số bi xanh hộp 1, n2_r: số bi đỏ hộp 2
            n1_g = random.choice([3, 4])
            n1_total = 8
            n1_r = n1_total - n1_g

            n2_g = 2
            n2_r = random.choice([3, 4])
            n2_total = n2_g + n2_r

            # Xác suất cho đề bài
            prob_box1_2g = Rational(binomial(n1_g, 2), binomial(n1_total, 2))
            prob_box2_2g = Rational(binomial(n2_g, 2), binomial(n2_total, 2))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Hộp thứ nhất có %s bi gồm bi xanh và bi đỏ và hộp thứ hai có %s bi xanh và một số bi đỏ. Các viên bi có kích thước và khối lượng như nhau. Chọn ngẫu nhiên từ mỗi hộp 2 viên bi. Xác suất để chọn được 2 bi xanh ở hộp thứ nhất là $%s$ và xác suất để chọn được 2 bi xanh ở hộp thứ hai là $%s$.''' 
                             %(latex(n1_total), latex(n2_g), latex(prob_box1_2g), latex(prob_box2_2g)))

            ########################################################################
            # Mệnh đề (a): Xác suất 2 xanh hộp 1 và 2 xanh hộp 2
            p_a_dung = prob_box1_2g * prob_box2_2g
            p_a_sai = p_a_dung + Rational(1, 70) if p_a_dung < Rational(1, 2) else p_a_dung - Rational(1, 70)

            nb_da_1_d = '\\True Xác suất để chọn được hai bi màu xanh ở hộp thứ nhất và hai bi màu xanh ở hộp thứ hai bằng $%s$' %(latex(p_a_dung))
            nb_da_1_s = 'Xác suất để chọn được hai bi màu xanh ở hộp thứ nhất và hai bi màu xanh ở hộp thứ hai bằng $%s$' %(latex(p_a_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Gọi $A$ là biến cố "Chọn được 2 bi xanh ở hộp thứ nhất và 2 bi xanh ở hộp thứ hai". \\\\
            Vì việc chọn bi ở mỗi hộp là độc lập nên $P(A) = %s \\cdot %s = %s$.''' 
                            %(latex(prob_box1_2g), latex(prob_box2_2g), latex(p_a_dung)))

            ########################################################################
            # Mệnh đề (b): Xác suất 2 đỏ ở hộp thứ nhất
            p_b_dung = Rational(binomial(n1_r, 2), binomial(n1_total, 2))
            p_b_sai = Rational(1, 28) if p_b_dung != Rational(1, 28) else Rational(3, 28)

            th_da_1_d = '\\True Xác suất để chọn được hai bi màu đỏ ở hộp thứ nhất bằng $%s$' %(latex(p_b_dung))
            th_da_1_s = 'Xác suất để chọn được hai bi màu đỏ ở hộp thứ nhất bằng $%s$' %(latex(p_b_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Số bi xanh ở hộp thứ nhất thỏa mãn: $\\frac{C_{n}^2}{C_{8}^2} = %s \\Rightarrow C_{n}^2 = %s \\Rightarrow n = %s$. \\\\
            Suy ra hộp thứ nhất có %s bi xanh và %s bi đỏ. \\\\
            Xác suất chọn 2 bi đỏ ở hộp thứ nhất là $\\frac{C_{%s}^2}{C_{8}^2} = %s$.''' 
                            %(latex(prob_box1_2g), latex(binomial(n1_g, 2)), latex(n1_g), latex(n1_g), latex(n1_r), latex(n1_r), latex(p_b_dung)))

            ########################################################################
            # Mệnh đề (c): 2 xanh hộp 1 và 2 đỏ hộp 2
            prob_box2_2r = Rational(binomial(n2_r, 2), binomial(n2_total, 2))
            p_c_dung = prob_box1_2g * prob_box2_2r
            p_c_sai = p_c_dung * Rational(2, 3)

            vd_da_1_d = '\\True Xác suất để chọn được hai bi màu xanh ở hộp thứ nhất và hai bi màu đỏ ở hộp thứ hai bằng $%s$' %(latex(p_c_dung))
            vd_da_1_s = 'Xác suất để chọn được hai bi màu xanh ở hộp thứ nhất và hai bi màu đỏ ở hộp thứ hai bằng $%s$' %(latex(p_c_sai))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Số bi đỏ ở hộp thứ hai thỏa mãn: $\\frac{C_{2}^2}{C_{m+2}^2} = %s \\Rightarrow C_{m+2}^2 = %s \\Rightarrow m+2 = %s \\Rightarrow m = %s$. \\\\
            Suy ra hộp thứ hai có %s bi đỏ. Xác suất chọn 2 bi đỏ ở hộp 2 là $\\frac{C_{%s}^2}{C_{%s}^2} = %s$. \\\\
            Xác suất cần tìm là: $%s \\cdot %s = %s$.''' 
                            %(latex(prob_box2_2g), latex(binomial(n2_total, 2)), latex(n2_total), latex(n2_r), latex(n2_r), latex(n2_r), latex(n2_total), latex(prob_box2_2r), latex(prob_box1_2g), latex(prob_box2_2r), latex(p_c_dung)))

            ########################################################################
            # Mệnh đề (d): Ít nhất một bi xanh
            p_d_khong_xanh = p_b_dung * prob_box2_2r
            p_d_dung = 1 - p_d_khong_xanh
            p_d_sai = Rational(6, 7) if p_d_dung != Rational(6, 7) else Rational(5, 7)

            vdc_da_1_d = '\\True Xác suất để chọn được ít nhất một bi màu xanh bằng $%s$' %(latex(p_d_dung))
            vdc_da_1_s = 'Xác suất để chọn được ít nhất một bi màu xanh bằng $%s$' %(latex(p_d_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Biến cố đối của "chọn được ít nhất một bi xanh" là "tất cả 4 bi chọn ra đều là màu đỏ". \\\\
            Xác suất để 2 bi hộp 1 màu đỏ là $%s$. \\\\
            Xác suất để 2 bi hộp 2 màu đỏ là $%s$. \\\\
            Xác suất để cả 4 bi màu đỏ là: $%s \\cdot %s = %s$. \\\\
            Vậy xác suất chọn được ít nhất một bi màu xanh là $1 - %s = %s$.''' 
                             %(latex(p_b_dung), latex(prob_box2_2r), latex(p_b_dung), latex(prob_box2_2r), latex(p_d_khong_xanh), latex(p_d_khong_xanh), latex(p_d_dung)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán vào list để đồng bộ với lời giải
            list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
            list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
            list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
            list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(list_nb_1[0])+'}\n'
                '{'+str(list_th_1[0])+'}\n'
                '{'+str(list_vd_1[0])+'}\n'
                '{'+str(list_vdc_1[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(list_nb_2[0])+'\n'
                '\\item '+str(list_th_2[0])+'\n'
                '\\item '+str(list_vd_2[0])+'\n'
                '\\item '+str(list_vdc_2[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

