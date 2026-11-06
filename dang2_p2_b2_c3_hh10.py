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


def bt_dang2_p2_b2_c3_hh10(self):
            # Khai báo biến
            xa=randint(-5,5)
            ya=randint(-5,5)
            xb=randint(-5,5)
            yb=ya+2
            a=randint(1,5) 
            b=randint(-5,-1)
            c=randint(-5,5)

            xn=(yb-ya)
            yn=(-xb+xa)

            goc=(abs(xn*a+yn*b))/(sqrt(xn**2+yn**2)*sqrt(a**2+b**2))
            goc1=(abs(xn*a+yn*b+1))/(sqrt(xn**2+yn**2)*sqrt(a**2+b**2))

            # Khai báo ẩn
            x, y = symbols('x y')

            # Nhập phương trình
            eq1 = Eq(xn*x + yn*y, xn*xa+yn*ya)
            eq2 = Eq(a*x +b*y, -c)

            # Giải hệ
            solution = solve((eq1, eq2), (x, y))
            n1=solution[x]
            n2=solution[y]
            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $(Oxy)$, cho đường thẳng $\\Delta: %sx+%sy+%s=0$ và hai điểm $A(%s;%s), B(%s;%s)$.'''                 
                            %(latex(a),latex(b),latex(c),latex(xa),latex(ya),latex(xb),latex(yb),
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đường thẳng $AB$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$' %(latex(yb-ya),latex(-xb+xa))
            nb_da_1_s = 'Đường thẳng $AB$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$' %(latex(xb-xa),latex(yb-ya))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $\\Vec{AB}=(%s;%s)$. \\\\
                            Suy ra đường thẳng $AB$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$.'''
                        %(latex(xb-xa),latex(yb-ya),
                        latex(yb-ya),latex(-xb+xa)
                            ))

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
            th_da_1_d = '\\True Đường thẳng $AB$ có phương trình là $%sx+%sy+%s=0$' %(latex(xn),latex(yn),latex(-xn*xa-yn*ya))  
            th_da_1_s = 'Đường thẳng $AB$ có phương trình là $%sx+%sy+%s=0$' %(latex(xn),latex(yn),latex(xn*xa+yn*ya))   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Phương trình đường thẳng $AB$ là \\\\
                            $%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %sx+%sy+%s=0$.'''       
                        %(latex(xn),latex(xa),latex(yn),latex(ya),
                        latex(xn),latex(yn),latex(-xn*xa-yn*ya)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Gọi $\\alpha$ là góc giữa hai đường thẳng, khi đó $\\cos \\alpha = %s$' %(latex(goc))  
            vd_da_1_s = 'Gọi $\\alpha$ là góc giữa hai đường thẳng, khi đó $\\cos \\alpha = %s$' %(latex(goc1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Vectơ pháp tuyến của đường thẳng $AB$ là $\\vec{n}=(%s;%s)$. \\\\
                            Vectơ pháp tuyến của đường thẳng $\\Delta$ là $\\vec{u}=(%s;%s)$. \\\\
                                Gọi $\\alpha$ là góc giữa hai đường thẳng, ta có \\\\
                                    $\\cos \\alpha =\\frac{\\left| %s \\cdot (%s)+%s \\cdot (%s)\\right|}{\\sqrt{(%s)^2+(%s)^2} \\sqrt{(%s)^2+(%s)^2}}=%s$.'''  
                        %(latex(xn),latex(yn),
                        latex(a),latex(b),
                        latex(xn),latex(a),latex(yn),latex(b),
                        latex(xn),latex(yn),latex(a),latex(b),latex(goc)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Đường thẳng $AB$ cắt đường thẳng $\\Delta$ tại điểm $\\left(%s;%s \\right)$' %(latex(n1),latex(n2)) 
            vdc_da_1_s = 'Đường thẳng $AB$ cắt đường thẳng $\\Delta$ tại điểm $\\left(%s;%s \\right)$' %(latex(n1),latex(n2+1)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Tọa độ giao điểm của hai đường thẳng $AB$ và $\\Delta$ là nghiệm của hệ phương trình \\\\
                            $\\heva{& %sx+%sy+%s=0 \\\\& %sx+%sy+%s=0} \\Leftrightarrow \\heva{& x=%s \\\\ & y=%s}$. \\\\
                                Vậy tọa độ giao điểm của hai đường thẳng là $\\left(%s;%s \\right)$.'''
                        %(latex(xn),latex(yn),latex(-xn*xa-yn*ya),
                        latex(a),latex(b),latex(c),
                        latex(n1),latex(n2),
                        latex(n1),latex(n2)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('--', '+').replace('1x', 'x').replace('1y', 'y')
            return content   

