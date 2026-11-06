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


def bt_dang2_p2_b2_c2_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x = symbols('x')
                y = symbols('y')
                listen1=['Hưng','Bình','Mạnh','Kha','Phi','Việt','Tuyên','Đại','Hải','Hòa','Lâm','Tuấn','Trường','Sơn','Nam','Thắng','Dương','Đức','Hùng','Dũng']
                ten=random.choice(listen1)

                a=randint(20,27)

                b=randint(17,25)

                k=randint(50,70)
                h=randint(101,200)

                x0=randint(1,5)
                y0=randint(1,6)

                x1=randint(1,3)
                y1=randint(1,4)

                x2=randint(3,9)
                y2=randint(2,9)


                while a+b>k or a*x0+b*y0<k or a*x0+b*y0>h or a*x1+b*y1>k or a*x2+b*y2<h:
                    a=randint(20,27)

                    b=randint(17,25)

                    k=randint(50,70)
                    h=randint(101,200)

                    x0=randint(1,5)
                    y0=randint(1,6)

                    x1=randint(1,2)
                    y1=randint(1,2)

                    x2=randint(3,9)
                    y2=randint(2,9)


                xa=Rational(k,a+b)
                ya=xa
                xb=Rational(h,a+b)
                yb=xb
                xc=0
                yc=Rational(h,b)
                xd=0
                yd=Rational(k,b)



                # Nội dung câu hỏi
                noidungcauhoi = ('Trong $1$ lạng thịt bò chứa $%s$ protein, $1$ lạng cá chứa $%s$ protein. Trung bình trong một ngày, một người đàn ông cần từ $%s$ đến $%s$ protein. '
                                'Theo lời khuyên của bác sĩ, để tốt cho sức khỏe thì không nên ăn thịt nhiều hơn cá. '
                                'Gọi $x,y$ lần lượt là số lạng thịt bò, lạng cá mà một người đàn ông ăn trong một ngày. '
                                %(latex(a),latex(b),latex(k),latex(h)
                                ))



                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Hệ bất phương trình ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là $\\heva{& %s x+ %s y\\ge %s \\\\& %s x+ %s y\\le %s \\\\& x\\le y\\\\ & x\\ge 0 \\\\& y\\ge0}$'%(latex(a),latex(b),latex(k),latex(a),latex(b),latex(h))
                nb_da_1_s = 'Hệ bất phương trình ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là $\\heva{& %s x+ %s y> %s \\\\& %s x+ %s y< %s \\\\& x\\le y\\\\ & x\\ge 0 \\\\& y\\ge0}$'%(latex(a),latex(b),latex(k),latex(a),latex(b),latex(h))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Hệ bất phương trình ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là $\\heva{& %s x+ %s y\\ge %s \\\\& %s x+ %s y\\le %s \\\\& x\\le y\\\\ & x\\ge 0 \\\\& y\\ge0}$'%(latex(a),latex(b),latex(k),latex(a),latex(b),latex(h))
                nb_da_2_s = 'Hệ bất phương trình ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là $\\heva{& %s x+ %s y\\ge %s \\\\& %s x+ %s y\\le %s \\\\& x< y\\\\ & x\\ge 0 \\\\& y\\ge0}$'%(latex(a),latex(b),latex(k),latex(a),latex(b),latex(h))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Hệ bất phương trình ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là $\\heva{& %s x+ %s y\\ge %s \\\\& %s x+ %s y\\le %s \\\\& x\\le y\\\\ & x\\ge 0 \\\\& y\\ge0}$. '
                                %(latex(a),latex(b),latex(k),latex(a),latex(b),latex(h)))
                loigiai_nb_2 = ('Hệ bất phương trình ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là $\\heva{& %s x+ %s y\\ge %s \\\\& %s x+ %s y\\le %s \\\\& x\\le y\\\\ & x\\ge 0 \\\\& y\\ge0}$. '
                                %(latex(a),latex(b),latex(k),latex(a),latex(b),latex(h)))
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là một tứ giác'
                th_da_1_s = 'Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là một ngũ giác'
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$  để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là một tứ giác'
                th_da_2_s = 'Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$  để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là một tam giác'
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$  để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là một tứ giác.'
                                ''' \\begin{center}
                                \\scalebox{0.5}{
                                \\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-1.0448129022656285,-1.0754871931374024) rectangle (8.057655956905412,6.069461481265661);
                \\fill[fill=black,pattern=north east lines,pattern color=black] (-1.,6.) -- (8.,6.) -- (8.,-1.) -- (-1.,-1.) -- cycle;
                \\fill[color=ffffff,fill=ffffff,fill opacity=1.0] (0.,4.6) -- (2.62,2.62) -- (1.7142857142857142,1.7142857142857142) -- (0.,3.) -- cycle;
                \\draw [line width=0.4pt] (-1.,6.)-- (8.,6.);
                \\draw (8.,6.)-- (8.,-1.);
                \\draw (8.,-1.)-- (-1.,-1.);
                \\draw [line width=0.4pt] (-1.,-1.)-- (-1.,6.);
                \\draw [line width=3.6pt,color=ffffff] (0.,4.6)-- (2.62,2.62);
                \\draw [color=ffffff] (2.62,2.62)-- (1.7142857142857142,1.7142857142857142);
                \\draw [line width=2.4pt,color=ffffff] (1.7142857142857142,1.7142857142857142)-- (0.,3.);
                \\draw [line width=1.2pt,color=ffffff] (0.,3.)-- (0.,4.6);
                \\draw (-0.7791494486185474,0.04309576958714759) node[anchor=north west] {$O$};
                \\draw (-0.48552142090335254,5.929638610925092) node[anchor=north west] {$y$};
                \\draw (7.400488466304738,-0.06876252668530741) node[anchor=north west] {$x$};
                \\draw (1.5978393471711254,1.5112359081631195) node[anchor=north west] {$A$};
                \\draw (2.9401389024405877,2.993358333773148) node[anchor=north west] {$B$};
                \\draw (0.017840912322695805,4.950878518541111) node[anchor=north west] {$C$};
                \\draw (-0.6533088653120354,2.9514114726709777) node[anchor=north west] {$D$};
                \\draw [line width=1pt] (-1.,3.75)-- (5.333333333333333,-1.);
                \\draw [line width=1pt] (7.446666666666666,-1.)-- (-1.,5.335);
                \\draw [line width=1pt] (-1.,-1.)-- (6.,6.);
                \\draw [->,line width=1.3pt] (0.,-1.) -- (0.,6.);
                \\draw [->,line width=1pt] (-1.,0.) -- (8.,0.);
            \\end{tikzpicture}}                                    
                                \\end{center}'''
                                )
                loigiai_th_2 = ('Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$  để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông là một tứ giác.'
                                ''' \\begin{center}
                                \\scalebox{0.5}{
                                \\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-1.0448129022656285,-1.0754871931374024) rectangle (8.057655956905412,6.069461481265661);
                \\fill[fill=black,pattern=north east lines,pattern color=black] (-1.,6.) -- (8.,6.) -- (8.,-1.) -- (-1.,-1.) -- cycle;
                \\fill[color=ffffff,fill=ffffff,fill opacity=1.0] (0.,4.6) -- (2.62,2.62) -- (1.7142857142857142,1.7142857142857142) -- (0.,3.) -- cycle;
                \\draw [line width=0.4pt] (-1.,6.)-- (8.,6.);
                \\draw (8.,6.)-- (8.,-1.);
                \\draw (8.,-1.)-- (-1.,-1.);
                \\draw [line width=0.4pt] (-1.,-1.)-- (-1.,6.);
                \\draw [line width=3.6pt,color=ffffff] (0.,4.6)-- (2.62,2.62);
                \\draw [color=ffffff] (2.62,2.62)-- (1.7142857142857142,1.7142857142857142);
                \\draw [line width=2.4pt,color=ffffff] (1.7142857142857142,1.7142857142857142)-- (0.,3.);
                \\draw [line width=1.2pt,color=ffffff] (0.,3.)-- (0.,4.6);
                \\draw (-0.7791494486185474,0.04309576958714759) node[anchor=north west] {$O$};
                \\draw (-0.48552142090335254,5.929638610925092) node[anchor=north west] {$y$};
                \\draw (7.400488466304738,-0.06876252668530741) node[anchor=north west] {$x$};
                \\draw (1.5978393471711254,1.5112359081631195) node[anchor=north west] {$A$};
                \\draw (2.9401389024405877,2.993358333773148) node[anchor=north west] {$B$};
                \\draw (0.017840912322695805,4.950878518541111) node[anchor=north west] {$C$};
                \\draw (-0.6533088653120354,2.9514114726709777) node[anchor=north west] {$D$};
                \\draw [line width=1pt] (-1.,3.75)-- (5.333333333333333,-1.);
                \\draw [line width=1pt] (7.446666666666666,-1.)-- (-1.,5.335);
                \\draw [line width=1pt] (-1.,-1.)-- (6.,6.);
                \\draw [->,line width=1.3pt] (0.,-1.) -- (0.,6.);
                \\draw [->,line width=1pt] (-1.,0.) -- (8.,0.);
            \\end{tikzpicture}}                                    
                                \\end{center} '''
                                )
                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Điểm $(%s;%s)$ thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông'%(latex(x0),latex(y0))
                vd_da_1_s = 'Điểm $(%s;%s)$ không thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông'%(latex(x0),latex(y0))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Điểm $(%s;%s)$ không thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông'%(latex(x2),latex(y2))
                vd_da_2_s = 'Điểm $(%s;%s)$ thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông'%(latex(x2),latex(y2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $(%s;%s)$ thỏa mãn tất cả các bất phương trình nên cặp số $(%s;%s)$ thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông.'
                                %(latex(x0),latex(y0),latex(x0),latex(y0),
                                ))
                loigiai_vd_2 = (' $(%s;%s)$ không thỏa mãn bất phương trình $%s x + %s y\\le %s $ của hệ nên cặp số $(%s;%s)$ không thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông.'
                                %(latex(x2),latex(y2),latex(a),latex(b), latex(h), latex(x2),latex(y2),
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Điểm $\\left(%s;%s\\right)$ là điểm có hoành độ lớn nhất thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông'%(latex(xb),latex(yb))
                vdc_da_1_s = 'Điểm $\\left(%s;%s\\right)$ là điểm có hoành độ lớn nhất thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông'%(latex(xa),latex(ya))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Điểm $\\left(%s;%s\\right)$ là điểm có tung độ bé nhất thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông'%(latex(xa),latex(ya))
                vdc_da_2_s = 'Điểm $\\left(%s;%s\\right)$ là điểm có tung độ bé nhất thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn $x,y$ để biểu diễn lượng protein cần thiết trong một ngày cho một người đàn ông'%(latex(xc),latex(yc))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 =('Miền nghiệm của bất phương trình là hình tứ giác $ABCD$ với $$A\\left(%s;%s\\right),B\\left(%s;%s\\right);C\\left(%s;%s\\right),D\\left(%s;%s\\right).$$'
                                'Vậy điểm có hoành độ lớn nhất là $B\\left(%s;%s\\right)$.'
                                %(latex(xa),latex(ya),latex(xb),latex(yb),latex(xc),latex(yc),latex(xd),latex(yd),
                                latex(xb),latex(yb)
                                ))
                loigiai_vdc_2 =('Miền nghiệm của bất phương trình là hình tứ giác $ABCD$ với $$A\\left(%s;%s\\right),B\\left(%s;%s\\right);C\\left(%s;%s\\right),D\\left(%s;%s\\right).$$'
                                'Vậy điểm có tung độ bé nhất là $A\\left(%s;%s\\right)$.'
                                %(latex(xa),latex(ya),latex(xb),latex(yb),latex(xc),latex(yc),latex(xd),latex(yd),
                                latex(xa),latex(ya)
                                ))
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

