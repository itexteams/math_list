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


def bt_dang4_p2_b1_c5_ds10(self):
            # Khai báo biến
            # n1: bút chì, n2: bút bi, n3: bút máy
            n1 = random.randint(3, 6)
            n2 = random.randint(4, 8)
            n3 = random.randint(2, 5)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong hộp bút của Lan có %s chiếc bút chì, %s chiếc bút bi và %s chiếc bút máy (tất cả đều khác nhau).''' 
                             %(latex(n1), latex(n2), latex(n3)))

            ########################################################################
            # Nhận biết - Câu (a): Chọn 1 chì và 1 bi
            ########################################################################
            ans_a_correct = n1 * n2
            ans_a_wrong = n1 + n2 # Sai do dùng quy tắc cộng

            nb_da_1_d = '\\True Số cách chọn 1 chiếc bút chì và 1 chiếc bút bi là %s (cách)' %(latex(ans_a_correct))
            nb_da_1_s = 'Số cách chọn 1 chiếc bút chì và 1 chiếc bút bi là %s (cách)' %(latex(ans_a_wrong))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Việc chọn 1 chiếc bút chì và 1 chiếc bút bi gồm 2 công đoạn: \\\\
                            - Công đoạn 1: Chọn 1 chiếc bút chì từ %s chiếc, có %s cách. \\\\
                            - Công đoạn 2: Chọn 1 chiếc bút bi từ %s chiếc, có %s cách. \\\\
                            Theo quy tắc nhân, số cách chọn là $%s \\cdot %s = %s$ (cách).''' 
                            %(latex(n1), latex(n1), latex(n2), latex(n2), latex(n1), latex(n2), latex(ans_a_correct)))
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu - Câu (b): Chọn 1 chì và 1 máy
            ########################################################################
            ans_b_correct = n1 * n3
            ans_b_wrong = n1 # Sai do chỉ tính số bút chì

            th_da_1_d = '\\True Số cách chọn 1 chiếc bút chì và 1 chiếc bút máy là %s (cách)' %(latex(ans_b_correct))
            th_da_1_s = 'Số cách chọn 1 chiếc bút chì và 1 chiếc bút máy là %s (cách)' %(latex(ans_b_wrong))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Việc chọn 1 chiếc bút chì và 1 chiếc bút máy gồm 2 công đoạn: \\\\
                            - Công đoạn 1: Chọn 1 chiếc bút chì có %s cách. \\\\
                            - Công đoạn 2: Chọn 1 chiếc bút máy có %s cách. \\\\
                            Theo quy tắc nhân, số cách chọn là $%s \\cdot %s = %s$ (cách).''' 
                            %(latex(n1), latex(n3), latex(n1), latex(n3), latex(ans_b_correct)))
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng - Câu (c): Chọn 1 bi và 1 máy
            ########################################################################
            ans_c_correct = n2 * n3
            ans_c_wrong = n2 + n3 + 2 # Sai số ngẫu nhiên

            vd_da_1_d = '\\True Số cách chọn 1 chiếc bút bi và 1 chiếc bút máy là %s (cách)' %(latex(ans_c_correct))
            vd_da_1_s = 'Số cách chọn 1 chiếc bút bi và 1 chiếc bút máy là %s (cách)' %(latex(ans_c_wrong))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Việc chọn 1 chiếc bút bi và 1 chiếc bút máy gồm 2 công đoạn: \\\\
                            - Công đoạn 1: Chọn 1 chiếc bút bi có %s cách. \\\\
                            - Công đoạn 2: Chọn 1 chiếc bút máy có %s cách. \\\\
                            Theo quy tắc nhân, số cách chọn là $%s \\cdot %s = %s$ (cách).''' 
                            %(latex(n2), latex(n3), latex(n2), latex(n3), latex(ans_c_correct)))
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao - Câu (d): Chọn 2 chiếc khác loại
            ########################################################################
            ans_d_correct = n1*n2 + n1*n3 + n2*n3
            ans_d_wrong = n1 + n2 + n3 # Sai do lấy tổng số bút

            vdc_da_1_d = '\\True Số cách chọn 2 chiếc bút khác loại với nhau từ hộp bút của Lan là %s (cách)' %(latex(ans_d_correct))
            vdc_da_1_s = 'Số cách chọn 2 chiếc bút khác loại với nhau từ hộp bút của Lan là %s (cách)' %(latex(ans_d_wrong))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Để chọn 2 chiếc bút khác loại, ta có các trường hợp sau: \\\\
                            - Trường hợp 1: Chọn 1 bút chì và 1 bút bi. Có $%s \\cdot %s = %s$ cách. \\\\
                            - Trường hợp 2: Chọn 1 bút chì và 1 bút máy. Có $%s \\cdot %s = %s$ cách. \\\\
                            - Trường hợp 3: Chọn 1 bút bi và 1 bút máy. Có $%s \\cdot %s = %s$ cách. \\\\
                            Vậy tổng số cách chọn là $%s + %s + %s = %s$ (cách).''' 
                             %(latex(n1), latex(n2), latex(n1*n2), 
                               latex(n1), latex(n3), latex(n1*n3), 
                               latex(n2), latex(n3), latex(n2*n3), 
                               latex(n1*n2), latex(n1*n3), latex(n2*n3), latex(ans_d_correct)))
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Gán lại vào list sau khi thỏa mãn điều kiện số câu đúng
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            shuffled_answers_nb = [nb_da_1]
            shuffled_answers_th = [th_da_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_answers_vdc = [vdc_da_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

