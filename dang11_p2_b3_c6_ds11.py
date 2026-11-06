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


def bt_dang11_p2_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            k = random.randint(2, 5) # Tỉ số xác suất sấp gấp k lần ngửa của đồng xu B
            p_na = Rational(1, 2)    # Xác suất ngửa đồng xu A
            p_nb = Rational(1, k + 1) # Xác suất ngửa đồng xu B: P(S)=kP(N) => (k+1)P(N)=1
            p_both_once = p_na * p_nb # Xác suất cả hai cùng ngửa 1 lần
            p_both_twice = p_both_once**2 # Xác suất cả hai cùng ngửa trong cả 2 lần gieo

            # Nội dung câu hỏi
            noidungcauhoi = ('''Gieo hai đồng xu $A$ và $B$ một cách độc lập. Đồng xu $A$ được chế tạo cân đối. Đồng xu $B$ được chế tạo không cân đối nên xác suất xuất hiện mặt sấp gấp %s lần xác suất xuất hiện mặt ngửa.''' 
                             % (latex(k)))

            ########################################################################
            # Nhận biết (Câu a)
            nb_da_1_d = '\\True Đồng xu $A$ xuất hiện mặt ngửa bằng $\\frac{1}{2}$'
            nb_da_1_s = 'Đồng xu $A$ xuất hiện mặt ngửa bằng $\\frac{1}{3}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Vì đồng xu $A$ cân đối và đồng chất nên xác suất xuất hiện mặt ngửa bằng xác suất xuất hiện mặt sấp và bằng $\\frac{1}{2}$.''')

            ########################################################################
            # Thông hiểu (Câu b)
            th_da_1_d = '\\True Đồng xu $B$ xuất hiện mặt ngửa bằng $%s$' % (latex(p_nb))
            th_da_1_s = 'Đồng xu $B$ xuất hiện mặt ngửa bằng $%s$' % (latex(Rational(1, k)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Gọi $P(N_B)$ là xác suất hiện mặt ngửa và $P(S_B)$ là xác suất hiện mặt sấp của đồng xu $B$. \\\\
                            Ta có $P(S_B) + P(N_B) = 1$. Vì $P(S_B) = %s P(N_B)$ nên $%s P(N_B) + P(N_B) = 1 \\Leftrightarrow %s P(N_B) = 1 \\Leftrightarrow P(N_B) = %s$.'''
                            % (latex(k), latex(k), latex(k+1), latex(p_nb)))

            ########################################################################
            # Vận dụng (Câu c)
            vd_da_1_d = '\\True Khi gieo hai đồng xu một lần thì cả hai đều ngửa bằng $%s$' % (latex(p_both_once))
            vd_da_1_s = 'Khi gieo hai đồng xu một lần thì cả hai đều ngửa bằng $%s$' % (latex(Rational(1, 2*k)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Do hai đồng xu được gieo độc lập nên xác suất để cả hai cùng ngửa trong một lần gieo là: \\\\
                            $P = P(N_A) \\cdot P(N_B) = \\frac{1}{2} \\cdot %s = %s$.'''
                            % (latex(p_nb), latex(p_both_once)))

            ########################################################################
            # Vận dụng cao (Câu d)
            vdc_da_1_d = '\\True Khi gieo hai đồng xu hai lần thì cả hai đồng xu đều ngửa trong cả hai lần bằng $%s$' % (latex(p_both_twice))
            vdc_da_1_s = 'Khi gieo hai đồng xu hai lần thì cả hai đồng xu đều ngửa trong cả hai lần bằng $%s$' % (latex(p_both_once * 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Xác suất để cả hai đồng xu đều ngửa trong một lần gieo là $P_1 = %s$. \\\\
                             Khi gieo hai lần độc lập, xác suất để cả hai lần gieo đều nhận được kết quả cả hai đồng xu cùng ngửa là: \\\\
                             $P = P_1 \\cdot P_1 = %s \\cdot %s = %s$.'''
                             % (latex(p_both_once), latex(p_both_once), latex(p_both_once), latex(p_both_twice)))

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

            # Gán lại vào list để xử lý logic giống mẫu
            list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
            list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
            list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
            list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(list_nb_1[0]) + '}\n'
                '{' + str(list_th_1[0]) + '}\n'
                '{' + str(list_vd_1[0]) + '}\n'
                '{' + str(list_vdc_1[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(list_nb_2[0]) + '\n'
                '\\item ' + str(list_th_2[0]) + '\n'
                '\\item ' + str(list_vd_2[0]) + '\n'
                '\\item ' + str(list_vdc_2[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

