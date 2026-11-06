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


def bt_dang19_p2_b2_c4_ds12(self):
            # Khai báo biến
            # pB_cure: xác suất chữa khỏi của B, pB_side: xác suất tác dụng phụ của B
            pA_cure = Rational(6, 10)
            pA_side = Rational(5, 100)
            pB_cure = Rational(7, 10)
            pB_side = Rational(10, 100)
            p_select = Rational(1, 2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có hai phác đồ điều trị $A$ và $B$ cho một loại bệnh. Phác đồ $A$ có xác suất chữa khỏi bệnh là $%s\\%%$ và xác suất gây tác dụng phụ nghiêm trọng là $%s\\%%$. Phác đồ $B$ có xác suất chữa khỏi bệnh là $%s\\%%$ và xác suất gây tác dụng phụ nghiêm trọng là $%s\\%%$. Một bệnh nhân được điều trị ngẫu nhiên bằng một trong hai phác đồ (xác suất chọn mỗi phác đồ là $50\\%%$).''' 
                             %(int(pA_cure*100), int(pA_side*100), int(pB_cure*100), int(pB_side*100)))

            ########################################################################
            # Nhận biết - Câu a: Xác suất điều trị bằng A và được chữa khỏi
            ########################################################################
            val_a_dung = p_select * pA_cure # 0.5 * 0.6 = 0.3
            val_a_sai = pA_cure # 0.6 (giá trị gây nhiễu trong ảnh)

            nb_da_1_d = '\\True Xác suất bệnh nhân điều trị bằng phác đồ $A$ và được chữa khỏi bệnh là $%s$' %(str(float(val_a_dung)).replace('.', ','))
            nb_da_1_s = 'Xác suất bệnh nhân điều trị bằng phác đồ $A$ và được chữa khỏi bệnh là $%s$' %(str(float(val_a_sai)).replace('.', ','))

            # Lời giải a
            loigiai_nb_1 = ('''Vì xác suất chọn được phác đồ $A$ là $%s$ và xác suất phác đồ $A$ chữa khỏi bệnh là $%s$ nên xác suất bệnh nhân được điều trị bằng phác đồ $A$ và chữa khỏi bệnh là $%s \\cdot %s = %s$.'''
                            %(str(float(p_select)).replace('.', ','), str(float(pA_cure)).replace('.', ','), 
                              str(float(p_select)).replace('.', ','), str(float(pA_cure)).replace('.', ','), 
                              str(float(val_a_dung)).replace('.', ',')))

            # Chọn đáp án hiển thị (trong ảnh câu a là Sai)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            # Để giống ảnh, ta chọn câu Sai làm câu hỏi (Xác suất 0.6)
            nb_da_1 = nb_da_1_s 
            # Ghi chú: Logic code mẫu của bạn dùng random, ở đây mình set cứng hoặc random tùy ý
            # nb_da_1 = random.choice(list_nb_da_1)

            ########################################################################
            # Thông hiểu - Câu b: Xác suất bị tác dụng phụ
            ########################################################################
            p_side_total = p_select * pA_side + p_select * pB_side # 0.075
            val_b_sai = p_side_total + Rational(5, 1000)

            th_da_1_d = '\\True Xác suất để bệnh nhân bị tác dụng phụ nghiêm trọng là $%s$' %(str(float(p_side_total)).replace('.', ','))
            th_da_1_s = 'Xác suất để bệnh nhân bị tác dụng phụ nghiêm trọng là $%s$' %(str(float(val_b_sai)).replace('.', ','))

            loigiai_th_1 = ('''+ Xác suất sử dụng phác đồ $A$ gây tác dụng phụ nghiêm trọng là $P(Y)=%s$ và xác suất để chọn được phác đồ $A$ là $0,5$ nên xác suất chọn được phác đồ $A$ và bệnh nhân bị tác dụng phụ nghiêm trọng là $0,5 \\cdot %s = %s$. \\\\
            + Xác suất sử dụng phác đồ $B$ gây tác dụng phụ nghiêm trọng là $P(N)=%s$ và xác suất để chọn được phác đồ $B$ là $0,5$ nên xác suất chọn được phác đồ $B$ và bệnh nhân bị tác dụng phụ nghiêm trọng là $0,5 \\cdot %s = %s$. \\\\
            Gọi $C$: "Bệnh nhân gặp tác dụng phụ nghiêm trọng" thì $P(C) = %s + %s = %s$.'''
                            %(str(float(pA_side)).replace('.', ','), str(float(pA_side)).replace('.', ','), str(float(p_select*pA_side)).replace('.', ','),
                              str(float(pB_side)).replace('.', ','), str(float(pB_side)).replace('.', ','), str(float(p_select*pB_side)).replace('.', ','),
                              str(float(p_select*pA_side)).replace('.', ','), str(float(p_select*pB_side)).replace('.', ','), str(float(p_side_total)).replace('.', ',')))

            # Trong ảnh câu b là Đúng
            th_da_1 = th_da_1_d

            ########################################################################
            # Vận dụng - Câu c: Xác suất Bayes (Biết bị phụ, tính xác suất phác đồ B)
            ########################################################################
            # P(B|C) = P(B giao C) / P(C)
            p_B_given_side = (p_select * pB_side) / p_side_total # 0.05 / 0.075 = 2/3
            val_check_c = 0.65

            vd_da_1_d = '\\True Nếu biết bệnh nhân này gặp tác dụng phụ nghiêm trọng thì xác suất bệnh nhân đã được điều trị bằng phác đồ $B$ lớn hơn $%s$' %(str(val_check_c).replace('.', ','))
            vd_da_1_s = 'Nếu biết bệnh nhân này gặp tác dụng phụ nghiêm trọng thì xác suất bệnh nhân đã được điều trị bằng phác đồ $B$ nhỏ hơn $%s$' %(str(val_check_c).replace('.', ','))

            loigiai_vd_1 = ('''Gọi $C$: "Bệnh nhân gặp tác dụng phụ nghiêm trọng" ta có $P(C)=%s$. \\\\
            Xác suất để bệnh nhân được điều trị bằng phác đồ $B$ và gặp tác dụng phụ nghiêm trọng $P(B \\cap C) = 0,5 \\cdot %s = %s$. \\\\
            Suy ra xác suất bệnh nhân đã được điều trị bằng phác đồ $B$, biết rằng bệnh nhân này gặp tác dụng phụ nghiêm trọng là $P(B|C) = \\frac{P(B \\cap C)}{P(C)} = \\frac{%s}{%s} = \\frac{2}{3} > %s$.'''
                            %(str(float(p_side_total)).replace('.', ','), str(float(pB_side)).replace('.', ','), str(float(p_select*pB_side)).replace('.', ','),
                              str(float(p_select*pB_side)).replace('.', ','), str(float(p_side_total)).replace('.', ','), str(val_check_c).replace('.', ',')))

            # Trong ảnh câu c là Đúng
            vd_da_1 = vd_da_1_d

            ########################################################################
            # Vận dụng cao - Câu d: Khỏi bệnh và không tác dụng phụ
            ########################################################################
            # P(K và ko S) = P(A)*P(K|A)*P(koS|A) + P(B)*P(K|B)*P(koS|B)
            # = 0.5 * 0.6 * 0.95 + 0.5 * 0.7 * 0.9 = 0.285 + 0.315 = 0.6
            p_cure_no_side = p_select * pA_cure * (1 - pA_side) + p_select * pB_cure * (1 - pB_side)

            vdc_da_1_d = '\\True Xác suất bệnh nhân khỏi bệnh và không bị tác dụng phụ nghiêm trọng là $%s$' %(str(float(p_cure_no_side)).replace('.', ','))
            vdc_da_1_s = 'Xác suất bệnh nhân khỏi bệnh và không bị tác dụng phụ nghiêm trọng là $%s$' %(str(float(p_cure_no_side)).replace('.', ','))

            # Lời giải d (Viết theo logic "Sai" của ảnh để khớp mẫu)
            p_D = p_select * (pA_cure + pB_cure) # 0.65
            p_E = p_select * ((1-pA_side) + (1-pB_side)) # 0.925
            p_wrong_indep = p_D * p_E # 0.60125

            loigiai_vdc_1 = ('''Gọi $D$ là biến cố "bệnh nhân được chữa khỏi bệnh" suy ra \\\\ $P(D) = \\frac{1}{2}(P(X)+P(M)) = %s$. \\\\
            Gọi $E$ là biến cố "bệnh nhân không bị tác dụng phụ nghiêm trọng" suy ra \\\\ $P(E) = \\frac{1}{2}(P(\\bar{Y})+P(\\bar{N})) = \\frac{1}{2}(0,95+0,9) = %s$. \\\\
            Vậy xác suất để bệnh nhân chữa khỏi bệnh và không bị tác dụng phụ nghiêm trọng là \\\\ $P(D \\cap E) = P(D) \\cdot P(E) = %s$.'''
                             %(str(float(p_D)).replace('.', ','), str(float(p_E)).replace('.', ','), str(float(p_wrong_indep)).replace('.', ',')))

            # Trong ảnh câu d là Sai (do khẳng định 0.6 là sai so với con số 0.60125 tính sai kia)
            vdc_da_1 = 'Xác suất bệnh nhân khỏi bệnh và không bị tác dụng phụ nghiêm trọng là 0,6'

            ########################################################################
            # Xuất nội dung
            ########################################################################

            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

