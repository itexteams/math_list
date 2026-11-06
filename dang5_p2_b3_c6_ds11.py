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


def bt_dang5_p2_b3_c6_ds11(self):
            # Khai báo biến
            p=randint(80,96)
            p1=p/100
            p2=round(1-p1,2)
            q=randint(80,96)
            q1=q/100
            q2=round(1-q1,2)
            while p==q:
                p=randint(80,96)
                p1=p/100
                p2=round(1-p1,2)
                q=randint(80,96)
                q1=q/100
                q2=round(1-q1,2)
            r=p1*q2+p2*q1
            lis1=['Dương','Chung','Đức','Hưng','Lâm','Sơn','Vang','Hiền','Duy','Phú']
            t1=random.choice(lis1)
            lis2=['Dũng','Bắc','Bảo','Páo','Chiến','Đạo','Hồng','Bình','Cảnh']
            t2=random.choice(lis2)
            # Nội dung câu hỏi
            noidungcauhoi = ('Hai xạ thủ %s và %s bắn vào cùng một tiêu ở hai thời điểm khác nhau với xác suất bắn trúng mục tiêu lần lượt là $%s$ và $%s$$zz$ '
                            'Xét các biến cố:\\\\ \n'
                            '\\hspace*{1cm} $A$: "Xạ thủ %s bắn trúng mục tiêu";\\\\ \n'
                            '\\hspace*{1cm} $B$: "Xạ thủ %s bắn trúng mục tiêu"$zz$\\\\ \n'

                            %(t1,t2,latex(p1),latex(q1),t1,t2)
                            )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\mathrm{P}(\\overline{A})=%s;\\mathrm{P}(\\overline{B})=%s$'%(latex(p2),latex(q2))
            nb_da_1_s = '$\\mathrm{P}(\\overline{A})=%s;\\mathrm{P}(\\overline{B})=%s$'%(latex(q2),latex(p2))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Theo bài ta có\\\\ \n'
                            '\\hspace*{1cm}$\\mathrm{P}(A)=%s;\\mathrm{P}(\\overline{A})=1-%s=%s;\\mathrm{P}(B)=%s;\\mathrm{P}(\\overline{B})=1-%s=%s$$zz$'
                            %(latex(p1),latex(p1),latex(p2),latex(q1),latex(q1),latex(q2))
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Hai biến cố $A$ và $B$ độc lập'
            th_da_1_s = ' Hai biến cố $A$ và $B$ không độc lập'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Hai biến cố $\\overline{A}$ và $\\overline{B}$ độc lập'
            th_da_2_s = ' Hai biến cố $\\overline{A}$ và $\\overline{B}$ không độc lập'
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Vì hai xạ thủ bắn ở hai thời điểm khác nhau nên các cặp biến cố $A$ và $B$, $\\overline{A}$ và $\\overline{B}$ là độc lập$zz$'
                        )
            loigiai_th_2 = ('Vì hai xạ thủ bắn ở hai thời điểm khác nhau nên các cặp biến cố $A$ và $B$, $\\overline{A}$ và $\\overline{B}$ là độc lập$zz$'
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d ='\\True Xác suất xạ thủ %s bắn trúng mục tiêu còn xạ thủ %s không bắn trúng mục tiêu là $%s$'%(t1,t2,latex(p1*q2))
            vd_da_1_s = 'Xác suất xạ thủ %s bắn trúng mục tiêu còn xạ thủ %s không bắn trúng mục tiêu là $%s$'%(t1,t2,latex(1-p1*q2))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Xác suất xạ thủ %s không bắn trúng mục tiêu còn xạ thủ %s bắn trúng mục tiêu là $%s$'%(t1,t2,latex(p2*q1))
            vd_da_2_s = 'Xác suất xạ thủ %s không bắn trúng mục tiêu còn xạ thủ %s bắn trúng mục tiêu là $%s$'%(t1,t2,latex(1-p2*q1))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True Xác suất để cả hai xạ thủ đều bắn trúng mục tiêu là $%s$'%(latex(p1*q1))
            vd_da_3_s =  'Xác suất để cả hai xạ thủ đều bắn trúng mục tiêu là $%s$'%(latex(1-p1*q1))
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)

            vd_da_4_d = '\\True Xác suất để cả hai xạ thủ đều bắn không trúng mục tiêu là $%s$'%(latex(p2*q2))
            vd_da_4_s =  'Xác suất để cả hai xạ thủ đều bắn không trúng mục tiêu là $%s$'%(latex(1-p2*q2))
            list_vd_da_4=[vd_da_4_d,vd_da_4_s]
            vd_da_4=random.choice(list_vd_da_4)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2,vd_da_3,vd_da_4]

            # Nội dung lời giải
            loigiai_vd_1 = ('Xác suất xạ thủ %s bắn trúng mục tiêu còn xạ thủ %s không bắn trúng mục tiêu là\\\\ \n'
                            '\\hspace*{1cm}$\\mathrm{P}(A\\overline{B})=\\mathrm{P}(A)\\cdot \\mathrm{P}(\\overline{B})=%s\\cdot %s=%s$$zz$'
                            %(t1,t2,latex(p1),latex(q2),latex(p1*q2))
                        )
            loigiai_vd_2 = ('Xác suất xạ thủ %s không bắn trúng mục tiêu còn xạ thủ %s bắn trúng mục tiêu là\\\\ \n'
                            '\\hspace*{1cm}$\\mathrm{P}(\\overline{A}B)=\\mathrm{P}(\\overline{A})\\cdot \\mathrm{P}(B)=%s\\cdot %s=%s$$zz$'
                            %(t1,t2,latex(p2),latex(q1),latex(p2*q1))
                        )
            loigiai_vd_3=('Xác suất để cả hai xạ thủ đều bắn trúng mục tiêu là\\\\ \n'
                            '\\hspace*{1cm}$\\mathrm{P}(AB)=\\mathrm{P}(A)\\cdot \\mathrm{P}(B)=%s\\cdot %s=%s$$zz$'
                        %(latex(p1),latex(q1),latex(p1*q1))
                        )
            loigiai_vd_4=('Xác suất để cả hai xạ thủ đều bắn không trúng mục tiêu là\\\\ \n'
                            '\\hspace*{1cm}$\\mathrm{P}(\\overline{AB})=\\mathrm{P}(\\overline{A})\\cdot \\mathrm{P}(\\overline{B})=%s\\cdot %s=%s$$zz$'
                        %(latex(p2),latex(q2),latex(p2*q2))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2,loigiai_vd_3,loigiai_vd_4]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Xác suất để ít nhất có một trong hai xạ thủ bắn trúng mục tiêu là $%s$'%(latex(1-p2*q2))
            vdc_da_1_s = 'Xác suất để ít nhất có một trong hai xạ thủ bắn trúng mục tiêu là $%s$'%(latex(p1*q2))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Xác suất để có đúng một xạ thủ bắn trúng mục tiêu là $%s$'%(latex(r))
            vdc_da_2_s = 'Xác suất để có đúng một xạ thủ bắn trúng mục tiêu là $%s$'%(latex(1-r))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Xác suất để ít nhất có một trong hai xạ thủ bắn trúng mục tiêu là\\\\ \n'
                            '\\hspace*{1cm}$\\mathrm{P}(A\\cup B)=1-\\mathrm{P}(\\overline{AB})=1-%s\\cdot %s=%s$$zz$'
                            %(latex(p2),latex(q2),latex(1-p2*q2))
                        )
            loigiai_vdc_2 = ('Xác suất để có đúng một xạ thủ bắn trúng mục tiêu là\\\\ \n'
                            '\\hspace*{1cm}$\\mathrm{P}(A\\overline{B}\\cup \\overline{A}B)=\\mathrm{P}(A\\overline{B})+\\mathrm{P}(\\overline{A}B)=%s\\cdot %s+%s\\cdot %s=%s$$zz$'
                            %(latex(p1),latex(q2),latex(p2),latex(q1),latex(r))
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zz$','.')
            return content

